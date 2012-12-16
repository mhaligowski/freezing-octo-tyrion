from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'tyrion.apps.storage.views.index'),
    url(r'^elfinder/', include('elfinder.urls')),
)