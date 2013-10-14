from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'wadehuang'


def order_list(request):
    return render_to_response('order_list.html', {}, RequestContext(request,
        {
        })
    )

def order_details(request):
    return render_to_response('order_details.html', {}, RequestContext(request,
        {
        })
    )