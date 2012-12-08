from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dupa.views.home', name='home'),
    # url(r'^dupa/', include('dupa.foo.urls')),
)

if settings.DEBUG: urlpatterns += patterns('', 
	url(r'^admin/', include(admin.site.urls)),
)
