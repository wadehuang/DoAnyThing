from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'wadehuang'

def user_details(request):
    return render_to_response('user_details.html', {}, RequestContext(request,
        {
        })
    )