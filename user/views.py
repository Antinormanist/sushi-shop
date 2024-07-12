from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, ChangeProfileForm, ChangeAvatar
from .models import Profile, User
# Create your views here.
@login_required(login_url='/user/login')
def profile(request):
    if request.method == 'POST':
        form_image = ChangeAvatar(request.POST, request.FILES, instance=request.user)
        if form_image.is_valid():
            form_image.save()
        else:
            form = ChangeProfileForm(request.POST)
            if form.is_valid():
                last_name = form.cleaned_data['last_name']
                first_name = form.cleaned_data['first_name']
                patronymic = form.cleaned_data['patronymic']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                # user_profile = Profile.objects.get(user=request.user)
                user_profile = Profile.objects.filter(user=request.user)
                user_profile.update(last_name=last_name, first_name=first_name,
                patronymic=patronymic, phone=phone, address=address)
        return redirect(reverse('user:profile'))
    else:
        form = ChangeProfileForm()
        form_image = ChangeAvatar()
    context = {
        'title': 'Profile',
        'no_footer': True,
        'form': form,
        'form_image': form_image,
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
            Profile.objects.create(
                user=user
            )
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