# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def dashboard(request):
    return render_to_response('dashboard.html', {}, RequestContext(request,
        {
            'test' : 'hehe'
        })
    )