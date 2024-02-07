from django.urls import path
from accounts_app.views import LoginView, register, LogoutView


app_name = 'accounts_app'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]