from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.contrib.auth import authenticate, login
from accounts_app.forms import RegisterForm


class LoginView(AuthLoginView):
    template_name = 'accounts_app/login.html'


class LogoutView(AuthLogoutView):
    template_name = 'accounts_app/logout.html'


def register(request):
    if request.method == "GET":
        form = RegisterForm
        context = {
            "form": form
        }
        return render(request, 'accounts_app/register.html', context=context)
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data().get("username")
            password = form.cleaned_data().get("password1")

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

            return redirect('/')


