from django.urls import path
from sweet_market_place_app.views import home_view, contact, add_to_cart, delete_product, shopping_cart, finalizeaza_comanda

app_name = 'sweet_market_place_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact, name='contact'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('finalizeaza_comanda/', finalizeaza_comanda, name='finalizeaza_comanda'),

    ]

