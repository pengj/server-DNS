from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from views import index, create, retrieve

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serverdns.views.home', name='home'),
    # url(r'^serverdns/', include('serverdns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #/
    url(r'^$', index, name='index'),
    # ex: /com.orange.onbill/to/10.0.1.87
    url(r'^(?P<pn>\S+)/to/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$', create, name='create'),
    # ex: /get/pname
    url(r'^get/(?P<pn>\S+)/$', retrieve, name='retrieve'),
)
