from django.shortcuts import render

from .models import Sushi

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'sushi': Sushi.objects.all(),
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'main/about.html', context)


def product(request, product_slug):
    context = {
        'title': 'Product',
    }
    return render(request, 'main/product.html', context)