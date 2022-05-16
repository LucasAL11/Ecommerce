from django.urls import path


from products import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='all_products'),    
    path('produto/<slug:slug>/', views.product_details, name='product_details' ),
    path('categoria/<slug:category_slug>/', views.per_category, name='per_category'),  
]