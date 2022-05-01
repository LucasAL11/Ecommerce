from django.shortcuts import render,get_object_or_404
from .models import Categories, Products

def categories(request):
    return {
        
            'categories': Categories.objects.all()
        }

def all_products(request):
    products = Products.products.all()
    return render(request, 'store/index.html', { 'products': products})

def product_details(request,slug):
    product = get_object_or_404(Products, Slug=slug, is_active=True)
    return render(request, 'store/single.html', {'product': product})

def per_category(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    product = Products.products.filter(category=category)
    return render(request, 'store/category.html',{'category':category,'product':product})
