from django.urls import path
from . import views

app_name = 'sweet_market_place_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    ]

