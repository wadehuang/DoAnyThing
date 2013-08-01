# Create your views here.
from allPowerful import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def dashboard(request):
    print settings.STATIC_DIR
    return render_to_response('dashboard.html', {}, RequestContext(request,
        {
            'test' : 'hehe'
        })
    )