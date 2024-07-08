from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
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