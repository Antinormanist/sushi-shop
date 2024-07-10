from django.shortcuts import render

# Create your views here.
def profile(request):
    context = {
        'title': 'Profile',
    }
    return render(request, 'user/profile.html', context)


def login(request):
    context = {
        'title': 'login',
    }
    return render(request, 'user/login.html', context)


def register(request):
    context = {
        'title': 'register',
    }
    return render(request, 'user/register.html', context)


def logout(request):
    ...