from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/', include('tyrion.apps.accounts.urls')),
	(r'^home/$', 'tyrion.apps.dashboard.views.index'),
    (r'^storage/', include('tyrion.apps.storage.urls')),
)

if settings.ENABLE_ADMIN: 
    urlpatterns += patterns('', 
	   url(r'^admin/', include(admin.site.urls)),
    )

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
    