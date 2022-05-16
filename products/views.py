from math import prod
from django.shortcuts import render,get_object_or_404

from .models import Category, PdtSpecValue, Products
 

def all_products(request):
    products = Products.objects.prefetch_related
    return render(request, 'store/index.html', {'products':products})

def per_category(request, category_slug=None):
    category = get_object_or_404(Category,slug=category_slug)
    category_slug = category_slug.replace('-',' ')
    print (category_slug)
    products = Products.objects.filter(
        category__in = Category.objects.get(name = category_slug).get_descendants(include_self=True)
    )
    return render(request,'store/category.html', {'category':category,'products':products})

def product_details(request, slug):
    
    product = get_object_or_404(Products, slug=slug, is_active=True)
    
    return render(request, 'store/single.html', {'product': product})

