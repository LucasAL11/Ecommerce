import json
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render

from cart.cart import Cart

from .models import Order, OrderItem

def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        cartTotal = cart.get_total_price()

        #verifica se existe o pedido

        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
                                address2='add2', total_paid=cartTotal, order_key=order_key)
            order_id = order.pk

            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        response = JsonResponse({'sucesso': 'ordem de pedido concluida'})

        return response  

def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).update(billing_status=True)
    return orders
