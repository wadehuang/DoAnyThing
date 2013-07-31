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
    url(r'^$', 'dashboard', name='dashboard'),
    url(r'^dashboard/$', 'dashboard', name='dashboard')
)

staticdir = settings.PROJECT_DIR + settings.CORE_ADDRESS + "/static"
urlpatterns += patterns('', url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': staticdir}), )
