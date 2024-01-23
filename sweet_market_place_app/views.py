from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'sweet_market_place_app/home.html')


