from argparse import Namespace
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('account/', include('users.urls', namespace='users')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('orders/', include('orders.urls', namespace='orders')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)