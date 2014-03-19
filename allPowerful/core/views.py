# coding: utf-8

# Create your views here.
from allPowerful import settings
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from core.forms.forms import LoginForm, UserForm
from core.tools.utils import get_next_url
from django.contrib.auth.models import AnonymousUser
import json


def index(request):
    return render_to_response('index.html', {}, RequestContext(request,
        {
            "active":"dashboard"
        })
    )

def logout(request):
    """Logs user out."""
    from django.contrib.auth import logout as djlogout
    loginForm = LoginForm()

    djlogout(request)
    return render_to_response('login.html', {}, RequestContext(request, {
        'formLogin': loginForm,
        }),
    )


def login(request):
    from django.contrib.auth import login as djlogin
    loginForm = LoginForm()
    errors = u""
    if request.method == 'POST':
        errors = u"请输入正确的账户密码"
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            auth_user = authenticate(username=loginForm.cleaned_data['username'],
                password=loginForm.cleaned_data['password'])

            if auth_user:
                # Authenticate user.
                if auth_user is not None:
                    if auth_user.is_active and not auth_user.is_superuser:
                        djlogin(request, auth_user)
                        request.session.set_expiry(settings.SESSION_EXPIRE_TIME)
                        next = get_next_url(request.META['HTTP_REFERER'])
                        if next:
                            return redirect(next)
                        else:
                            return redirect('/index/')
    if request.user != AnonymousUser():
        if not request.user.is_superuser:
            return redirect("/index/")

    return render_to_response("login.html", RequestContext(request, {
        'formLogin': loginForm,
        'errors': errors})
    )

#http://stackoverflow.com/questions/3523745/best-way-to-do-register-a-user-in-django
def register(request):
    is_success = False
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            is_success = True
    return render_to_response('register.html', {}, RequestContext(request,
        {
            'user_form':user_form,
            'is_success': is_success
        })
    )

def reset_password(request):
    pass


def get_ip_address(request):

    remote_addr = request.META.get("REMOTE_ADDR", None)
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", None)
    dict = {'remote_addr': remote_addr, 'x_forwarded_for':x_forwarded_for}
    return HttpResponse(json.dumps(dict))