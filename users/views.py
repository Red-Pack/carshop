from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import ProfileUpdateForm
from shop.models import Order
from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm

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
            return redirect("car:car_list")  # Перенаправляем на главную
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("car:car_list") 

def order_history(request):
    # Получаем заказы текущего пользователя (если пользователь не авторизован – можно перенаправлять на страницу входа)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'users/order_history.html', {'orders': orders})

@login_required
def profile_view(request):
    # Автоматически получаем текущего пользователя
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            instance=request.user
        )
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('user:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'users/profile_edit.html', {
        'form': form,
        'password_changed': request.GET.get('password_changed')
    })