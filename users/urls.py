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

    #password reset without login
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/user/password_reset_form.html',
                                                                success_url='password_reset_email_confirm',
                                                                email_template_name='account/user/password_reset_email.html',
                                                                form_class=PwdResetForm),name='pwdreset'),

    
    path('passsword_reset_comfirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',
                                                                                                success_url='password_reset_complete/',
                                                                                                form_class=PwdResetConfirmForm),name='pwdresetc'),
    

    
    path('password_reset/password_reset_email_confirm', TemplateView.as_view(template_name='account/user/reset_status.html'),name='password_reset_done'),
    path('password_reset_complete/', TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_complete'),


    #profile
    path('profile/', views.profile, name ='profile'),
    path('profile/edit/', views.edit_details, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_comfirmation', TemplateView.as_view(template_name='account/user/delete_confirmation.html'), name='delete_confirmation'),
    #path('profile/change_password/', template_name="account/user/change_password.html", success_url='password_reseted', form_class=PwdChangeForm),name='pwdchange')
    #path acima e relacionado a troca de senha que pode talvez ser subistituido por um sucess_url
]