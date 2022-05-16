from unicodedata import name
from django import forms 
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


from .models import(
    Category,
    Products,
    PdtImage,
    ProductSpec,
    PdtSpecValue,
    ProductType,
)

admin.site.register(Category, MPTTModelAdmin)

class PdtSpecOnline(admin.TabularInline):
    model = ProductSpec

@admin.register(ProductType)
class PdtTypeAdmin(admin.ModelAdmin):
    inlines = [
        PdtSpecOnline,
    ]

class PdtImageInLine(admin.TabularInline):
    model = PdtImage

class PdtSpecValueInline(admin.TabularInline):
    model = PdtSpecValue

@admin.register(Products)
class PdtAdmin(admin.ModelAdmin):
    inlines = [
        PdtSpecValueInline,
        PdtImageInLine,
    ]
    prepopulated_fields = {'slug':('name',)}


