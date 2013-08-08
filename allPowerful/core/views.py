# Create your views here.
from allPowerful import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
    return render_to_response('index.html', {}, RequestContext(request,
        {

        })
    )

def login(request):
    return render_to_response('login.html', {}, RequestContext(request,
        {

        })
    )

def register(request):
    return render_to_response('register.html', {}, RequestContext(request,
            {

        })
    )