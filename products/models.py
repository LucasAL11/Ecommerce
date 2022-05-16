from os import F_OK
from unicodedata import decimal
from django.db import models
from django.urls import reverse
from django.utils.translation import  gettext_lazy as _
from mptt.models import  MPTTModel,TreeForeignKey

import products

class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_("Category name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name=_("Category safe URL"),
        max_length=255,
        unique=True,
        )

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Categoty')
        verbose_name_plural = _('Categories')

    def get_absolute_url(self):
        return reverse('products:per_category',args=[self.slug])
    
    def __str__(self):
        return self.name

    

class ProductType(models.Model):
    name = models.CharField(
        verbose_name= _('Product type'),
        help_text= _('Required'),
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Product type')
        verbose_name_plural = _('Products types')
    
    def __str__(self):
        return self.name

class ProductSpec(models.Model):

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_('Required'),
        max_length=255
        )

    verbose_name = _('product specificantion')
    verbose_name_plural = _('products specifications')

    def __str__(self):
        return self.name    

class Products(models.Model):

    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_('Product Name'),
        help_text=_('Required'),
        max_length=255
    )
    slug = models.SlugField(max_length=255,default='')
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('not required'),
        blank = True,
        )

    original_price = models.DecimalField(
        verbose_name=_('original price'),
        help_text=('maximum 9999'),
        error_messages={
            'max_length':_('This price must bebetween 0 and 999999.99'),
        },
        max_digits=9,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        verbose_name=_('discount price'),
        help_text=('maximum 9999'),
        error_messages={
            'max_length':_('This price must bebetween 0 and 999999.99'),
        },
        max_digits=9,
        decimal_places=2
    )
    is_active = models.BooleanField(
        verbose_name=_('Product is active (this will show the products in website)'),
        help_text=_('change product visibility'),
        default=True,
    )
    created_at = models.DateTimeField(_("created_at"), auto_now=True ,editable=False)
    update_at = models.DateField(_('Updated at'), auto_now=True)

    class Meta:
        
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    def get_absolute_url(self):
        return reverse('products:product_details', args=[self.slug])
    
class PdtSpecValue(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpec, on_delete=models.CASCADE)
    value = models.CharField(
        verbose_name=_('value'),
        help_text=_('Product specification value(maximum of 255 woords)'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('Product specificatin value')
        verbose_name_plural = _('Product specification Values')
    
    def __str__(self):
        return self.value


class PdtImage(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="Product_image")
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_('Upload a product image'),
        upload_to='images/',
        default='images/default.png',
    )
    alt_text = models.CharField(
        verbose_name=_('Alternative text'),
        help_text=_('Please add a alternative text'),
        max_length=255,
        null=True,
        blank=True,
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural=_('Prodct images')


#estoque
#class PdtStock(models.Model):
#    product = models.ForeignKey(Products)
#    quantity = models.DecimalField(max_digits=999, decimal_places=0)
#    brand = models.Charfield()
#    minimum_stock = 
#    unity_cost
#    unity_price

#fornecedores
#class Supplier(models.model):
#   supplier = vc
#   phone = vc
#   product = pk
#   mail = vc
#   country
#   state
#   city
#   province
#   street
#   number

#entrada de financeiro
#class inners
#    date = date
#    product = fk
#    supplier = fk
#    quantity 
#    unity_cost
#    total


#class outers
#    date = date
#    product = fk
#    quantity_sold
#    in_stock
#    unity_cost
#    total

#class stock_control
#https://www.youtube.com/watch?v=_ebPqXfu_tY
#https://www.youtube.com/watch?v=br2Ups-TCWQ                