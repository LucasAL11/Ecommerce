from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db import models
from .models import Categories,Brands,Products,Distributors

# Register your models here.
@admin.register(Categories)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    populated_fields = {'slug': ('category',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product','brand','distributor','price','quantity_in_stock']
    prepopulated_fields = {'Slug': ('product',)}

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ['brand']

@admin.register(Distributors)
class DistributorAdmin(admin.ModelAdmin):
    pass

