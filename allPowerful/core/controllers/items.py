from django.shortcuts import render_to_response
from django.template import RequestContext

def item_details(request, id=None, item_type=None):
    return render_to_response('item_details.html', {}, RequestContext(request,
        {
            "active":""
        })
    )

def forward_item_page(request, item_type=None):
    item_list = []
    for i in range(2, 20):
        item_list.append(i)
    return  render_to_response('item_index.html', {}, RequestContext(request,
        {
            "item_list" : item_list,
            "active":item_type
        })
    )