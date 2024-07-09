from django.shortcuts import render
from django.db.models import Q

from .models import Sushi
from .utils import q_search

# Create your views here.
def index(request, sushi_type=None):
    
    if sushi_type:
        sushi = Sushi.objects.filter(type=sushi_type)
    else:
        sushi = Sushi.objects.all()
    if request.GET.get('nav'):
        price_order = request.GET.get('order-by-1')
        rank_order = request.GET.get('order-by-2')
        search = request.GET.get('search')
        if search:
            sushi = sushi.filter(q_search(sushi, search))
        if price_order:
            if price_order == 'asc':
                sushi = sushi.order_by('price')
            else:
                sushi = sushi.order_by('-price')
        if rank_order:
            sushi = sushi.filter(rate=int(rank_order))
    
    
    context = {
        'title': 'Home',
        'sushi': sushi
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