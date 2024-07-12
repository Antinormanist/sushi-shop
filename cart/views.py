from django.shortcuts import render

from .models import Cart
# Create your views here.
def cart(request):
    context = {
        'title': 'Cart',
        'products': Cart.objects.filter(user=request.user),
        'total_price': Cart.get_total_price(user=request.user),
    }
    return render(request, 'cart/cart.html', context)