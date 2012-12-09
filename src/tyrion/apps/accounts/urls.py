from django.conf.urls import patterns, include, url
from django.conf import settings

from userena import views as userena_views

import views

urlpatterns = patterns('',
	url(r'^signin/$', views.signin, { 'template_name': 'signin.html'}),
	url(r'^signout/$', userena_views.signout, name='userena_signout'),
)