from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Cart
from main.models import Sushi
# Create your views here.
@login_required
def cart(request):
    if request.method == 'GET' and (product_id := request.GET.get('delete')):
        Cart.objects.filter(id=product_id).delete()
    context = {
        'title': 'Cart',
        'products': Cart.objects.filter(user=request.user),
        'total_price': Cart.get_total_price(user=request.user),
    }
    return render(request, 'cart/cart.html', context)


@login_required
def order_make(request):
    if request.method == 'POST':
        name = request.POST.get('sushiName')
        description = request.POST.get('sushiDescription')
        amount = request.POST.get('amount')
        if name and description and amount:
            Cart.objects.create(
                user=request.user,
                amount=int(amount),
                sushi=Sushi.objects.get(name=name, description=description)
            )
    
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})