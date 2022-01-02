from django.db import models
from django.conf import settings
from django.db.models.fields import CharField, SlugField
from django.urls import reverse
from PIL import Image


# Create your models here.


class ActiveProductFitler(models.Manager):
    def get_queryset(self):
        return super(ActiveProductFitler, self).get_queryset().filter(is_active = True)

class Categories(models.Model):
    category = models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('products:per_category', args=[self.slug])

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category


class Brands(models.Model):
    brand = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.brand

class Distributors(models.Model):
    distributor = models.CharField(max_length=50,null=True)
    
    class Meta:
        verbose_name = 'Distribuidora'
        verbose_name_plural = 'Distribuidoras'
    
    def __str__(self):
        return self.distributor


class Products(models.Model):
    category = models.ForeignKey(Categories,related_name='produto', on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    distributor = models.ForeignKey(Distributors,on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    brand=  models.ForeignKey(Brands,on_delete=models.CASCADE)
    sku =   models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    Slug =  models.SlugField(max_length=50)
    products = ActiveProductFitler()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')


    class Meta:
        verbose_name_plural = 'Produtos'
        ordering = ('-create_date',)

    def get_absolute_url(self):
        return reverse('products:product_details', args=[self.Slug])

    def __str__(self):
        return self.product