#Gerenciador de formularios do APP user
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.fields import EmailField
from django.forms.widgets import TextInput
from .models import UserBase


#formulario de login
class UserLoginForm(AuthenticationForm):
    #define que a variavel username sera um campo de texto e seus atributos cs
    username = forms.CharField(widget=forms.TextInput(attrs=
    {
        'class':'form=control mb-3',
        'placeholder': 'usuario',
        'id': 'login-username' 
    }))
    password  = forms.CharField(widget=forms.PasswordInput(attrs=
    {
        'class' : 'form-control',
        'placeholder' : 'password',
        'id' : 'login-pwd'
    }))

class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(
        label='nome do usuario',
        min_length=4, 
        max_length=50, 
        help_text='campo obrigatorio'
        )

    email = forms.EmailField(
        max_length=100, 
        help_text='Required', 
        error_messages=
        {
            'required': 'favor preencher o campo'
        })

    password = forms.CharField(
        label='senha',
        widget=forms.PasswordInput,
        error_messages =
        {
            'required': 'Favor preencher o campo'
        })

    password2 = forms.CharField(
        label='comfirmar senha', 
        widget=forms.PasswordInput,
        error_messages={
            'required':'Favor preencher o campo'
        })

    class Meta:
        model = UserBase
        fields = (
            'user_name',
            'email',
            )

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("usuario ja esxistente")
        return user_name

    def clean_password(self):
        pwd = self.cleaned_data['password']
        

        if len(pwd) < 8:
            self.add_error('password', 'a senha e muito curta')
        elif not any (c.isupper() for c in pwd):
            self.add_error('password', 'A senha deve conter 1 caracter maiusculo')
        elif not any(c.islower() for c in pwd):
            self.add_error('password', 'a senha dever conter 1 caracter minusculo')
        elif not any (c.isdigit() for c in pwd):
            self.add_error('password', 'a senha deve contem pelo menos um numero')
        
        return pwd
        
    def clean_password2(self):
        pwd = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']
        if pwd != pwd2 and pwd2 != pwd: 
            self.add_error('password2','Senha diferem')
            print(pwd2)
            print(pwd)
            
        return pwd2
        
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            self.add_error('email', 'Email ja esta em uso')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Usuario'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'senha'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'comfirmar senha'})

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class PwdResetForm(PasswordResetForm):
    
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        useremail = UserBase.objects.filter(email=email)
        if not useremail: 
            raise forms.ValidationError('email invalido')
        return email

class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Email', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Nome completo', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'nome completo', 'id': 'form-user-name'}))

    class Meta:
        model = UserBase
        fields = ('email', 'user_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['user_name'].required = True


