from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MesajForm
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from .forms import OrderItemForm
from django.http import JsonResponse
from products_app.models.product import Product
from django.urls import reverse
from django.db.models import F

# Create your views here.
def home_view(request):
    return render(request, 'sweet_market_place_app/home.html')


def contact(request):
    if request.method == 'POST':
        form = MesajForm(request.POST)
        if form.is_valid():
            mesaj_nou = form.save(commit=False)
            mesaj_nou.status = 'necitit'
            mesaj_nou.save()
            return redirect('/')  # Redirecționează la pagina de contact sau altă pagină
    else:
        form = MesajForm()

    return render(request, 'sweet_market_place_app/contact.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    try:
        # Obține produsul pe baza id-ului
        product = get_object_or_404(Product, id=product_id)

        # Verifică dacă există deja un OrderItem pentru acest produs și utilizator
        order_item, created = OrderItem.objects.get_or_create(
            user=request.user,
            ordered=False,
            product=product
        )

        if created:
            messages.success(request, f"{product.name} a fost adăugat în coș.")
        else:
            # Dacă OrderItem există deja, actualizează cantitatea
            order_item.quantity = F('quantity') + 1
            order_item.save()
            messages.info(request, f"Cantitatea pentru {product.name} a fost actualizată în coș.")

        # Redirecționează către pagina coșului de cumpărături
        return redirect(reverse('sweet_market_place_app:shopping_cart'))
    except Exception as e:
        # Poți gestiona eroarea și returna un răspuns corespunzător
        messages.error(request, f"Eroare la adăugarea produsului în coș: {str(e)}")
        return redirect('/')

@login_required
def create_order(request):
    form = OrderItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            product_id = form.cleaned_data['product'].id
            quantity = form.cleaned_data['quantity']

            order_item, created = OrderItem.objects.get_or_create(
                user=request.user,
                ordered=False,
                product_id=product_id,
            )
            order_item.quantity += quantity
            order_item.save()

            return JsonResponse({'status': 'success'})

    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    order_total = sum(item.get_final_price() for item in order_items)

    context = {
        'form': form,
        'order_items': order_items,
        'order_total': order_total,
    }
    return render(request, 'sweet_market_place_app/shopping_cart.html', context)



def finalizeaza_comanda(request):
    if request.method == 'POST':
        # Preia elementele de comandă neachiziționate pentru utilizatorul autentificat
        order_items = OrderItem.objects.filter(user=request.user, ordered=False)

        # Creează o nouă comandă în baza de date cu elementele din coș
        new_order = Order.objects.create(user=request.user, ordered=True)
        new_order.items.set(order_items)

        # Actualizează starea elementelor de comandă la "ordered"
        order_items.update(ordered=True)

        messages.success(request, 'Comanda a fost plasată cu succes!')
        return redirect(reverse('sweet_market_place_app:home')) # Schimbă această redirecționare cu cea dorită

    # Redirecționează către o altă pagină sau întoarce un răspuns corespunzător
    return redirect(reverse('sweet_market_place_app:home')) # Schimbă această redirecționare cu cea dorită

def shopping_cart(request):
    # Obțineți toate elementele de comandă neachiziționate pentru utilizatorul autentificat
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)

    # Calculați totalul comenzii
    order_total = sum(item.get_final_price() for item in order_items)

    context = {
        'order_items': order_items,
        'total_cumparaturi': order_total,
    }

    return render(request, 'sweet_market_place_app/shopping_cart.html', context)

@login_required
def delete_product(request, product_id):
    if request.method == 'DELETE':
        try:
            order_item = OrderItem.objects.get(user=request.user, product_id=product_id, ordered=False)
            order_item.delete()
            return JsonResponse({'status': 'success'})
        except OrderItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Produsul nu a fost găsit în coș'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Metoda solicitată nu este permisă'})





