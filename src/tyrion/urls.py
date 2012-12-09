from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/', include('tyrion.apps.accounts.urls'))
)

if settings.DEBUG: urlpatterns += patterns('', 
	url(r'^admin/', include(admin.site.urls)),
)
