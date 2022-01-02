from django.contrib.auth import base_user
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

from django.db import models

from django.core.mail import send_mail
from django.db.models.fields.related import ForeignKey

from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField


class AccounteManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'a conta não tem os requisitos necessarios.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'a conta não tem os requisitos necessarios.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser,PermissionsMixin):
        
    email = models.EmailField(_('email addres'), unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)


    Country = CountryField()
    postcode = models.CharField(max_length=8, blank=True)
    address = models.CharField(_('adress'), max_length=20, blank=True) 
    city = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(_('Phone number'), max_length=20, blank=True)
        
    #status da conta do usuario

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AccounteManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'user_name'
    ]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )
    
    def __str__(self):
        return self.user_name    
    

 
    

  

# Create your models here.
