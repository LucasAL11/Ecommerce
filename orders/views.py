import json
from urllib import response
from webbrowser import get
from django.http import JsonResponse
from django.shortcuts import render

from cart.cart import Cart

from .models import Order, OrderItem

def add(request):
    cart = Cart(request)
    if request.method == 'POST':

        order_key = request.POST.get('order_key')
        data = {
            #data reciveid forom ajax
        }
        user_id = request.user.id
        name = request.user.user_name
        cartTotal = cart.get_total_price()

        #verify existents orders

        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name=name, district='district',
                                street='street',number='245',city='city',complement='fakedata', phone="99-88888-7777",cep='12345678', total_paid=cartTotal, order_key=order_key)
            order_id = order.pk

            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        response = JsonResponse({'sucesso': 'ordem de pedido concluida'})

        return response  

def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    
    return orders
