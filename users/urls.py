from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import (UserLoginForm)
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
    #Dashboard
    path('dashboard/', views.dashboard, name ='dashboard'),

]