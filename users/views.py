from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")  # Перенаправляем на главную
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login") 
