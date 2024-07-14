from decimal import Decimal

from django.shortcuts import render, reverse, redirect 
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

from .models import Cart
from main.models import Sushi

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION
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


@login_required
def payment(request):
    profile = request.user.profile
    if (profile.first_name != 'anonymous' and profile.last_name != 'anonymous' and 
        profile.patronymic != 'anonymous' and profile.address and profile.phone):
        # Do something
        session_data = {
            'mode': 'payment',
            'success_url': request.build_absolute_uri(reverse('success')),
            'cancel_url': request.build_absolute_uri(reverse('fail')),
            'line_items': []
        }
        
        products = Cart.objects.filter(user=request.user)
        for product in products:
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(product.sushi.price * Decimal(100)),
                    'currency': 'rub',
                    'product_data': {
                        'name': product.sushi.name,
                    },
                },
                'quantity': product.amount
            })
            
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        return HttpResponse('<h1>Не вся информация в профиле заполненна!</h1>')
    
    
def fail(request):
    return render(request, 'cart/fail.html')


def success(request):
    return render(request, 'cart/success.html', {'location': reverse('user:profile')})