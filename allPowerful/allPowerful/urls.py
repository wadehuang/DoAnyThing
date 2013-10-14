import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'allPowerful.views.home', name='home'),
    # url(r'^allPowerful/', include('allPowerful.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(r'^index/$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^register/$', 'register', name='register'),
    url(r'^reset_password/$', 'reset_password', name='reset_password'),
)

urlpatterns += patterns('core.controllers.items',
    url(r'^items/(?P<item_type>\w+)/(?P<id>\d+)/$', 'item_details', name='item_details'),
    url(r'^items/(?P<item_type>\w+)/index/$', 'forward_item_page', name='item')
)

urlpatterns += patterns('core.controllers.orders',
    url(r'^order_list/$', 'order_list', name='order_list'),
    url(r'^order_details/$', 'order_details', name='order_details')
)

urlpatterns += patterns('core.controllers.user',
    url(r'^user_details/$', 'user_details', name='user_details')
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR}),
)
