from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView
from .forms import (UserLoginForm, PwdResetForm, PwdResetConfirmForm)
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/user/login.html',
     form_class=UserLoginForm), 
     name='login'
     ),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('register/',views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),

      #redefinir senha
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/user/password_reset_form.html',
                                                                success_url='password_reset_email_confirm',
                                                                email_template_name='account/user/password_reset_email.html',
                                                                form_class=PwdResetForm),name='pwdreset'),

    path('passsword_reset_comfirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',
                                                                                                success_url='password_reset_complete/',
                                                                                                form_class=PwdResetConfirmForm),name='pwdresetc'),

    #Dashboard
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('profile/edit/', views.edit_details, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_comfirmation', TemplateView.as_view(template_name='account/user/delete_confirmation.html'), name='delete_confirmation'),
   

]