from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
# Create your views here.
@login_required(login_url='/user/login')
def profile(request):
    context = {
        'title': 'Profile',
    }
    return render(request, 'user/profile.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('user:profile'))
    
    context = {
        'title': 'login',
    }
    return render(request, 'user/login.html', context)


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('user:profile'))
    else:
        form = CreateUserForm()
        
    context = {
        'title': 'register',
        'form': form
    }
    return render(request, 'user/register.html', context)


@login_required(login_url='/user/login')
def logout_user(request):
    logout(request)
    return redirect('main:index')