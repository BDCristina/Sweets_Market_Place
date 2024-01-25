from django.urls import path
from .views import LogoutView, LoginView, register


app_name = 'accounts_app'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
]