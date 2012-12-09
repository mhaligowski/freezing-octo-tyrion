from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/', include('tyrion.apps.accounts.urls')),
	(r'^home/$', 'tyrion.apps.dashboard.views.index'),
    (r'^storage/$', 'tyrion.apps.storage.views.index'),
)

if settings.DEBUG: urlpatterns += patterns('', 
	url(r'^admin/', include(admin.site.urls)),
)
