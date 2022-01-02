
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


#from orders.views import user_orders

from .forms import RegistrationForm
from .models import UserBase
from .tokens import account_activation_token

# Create your views here.

@login_required
def dashboard(request):
        #orders = user_orders(request)
        return render(request,'account/user/dashoboard.html',
            {
                #'section': 'profile', 'orders': orders
            }
        )


def account_register(request):

    if request.user.is_authenticated:
        return redirect('users:dashboard')

    if request.method == "POST":
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            #email activation link
            current_site = get_current_site(request)
            subject = 'Ative sua conta'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            
            return HttpResponse('Registrado com sucesso, ative sua conta')
    else:
        registerForm = RegistrationForm()
    return render(request,'account/registration/register.html', {'forms': registerForm})


def account_activate(request, uidb64, token):
    #try to get the user in the DB 
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('users:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')