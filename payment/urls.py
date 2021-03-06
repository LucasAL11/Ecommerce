from django.urls import path

from . import views
from cart.cart import Cart

app_name = 'payment'


urlpatterns = [
     path('', views.PaymentHome, name='payment'), 
     path('orderplaced/', views.order_placed, name='orderplaced'),
     path('error/', views.Error.as_view(), name='error'),
     path('webhook/', views.stripe_webhook),
]  

