from django.conf.urls import patterns, include, url
from django.conf import settings

from userena import views as userena_views

urlpatterns = patterns('',
	url(r'^signin/$', userena_views.signin, { 'template_name': 'signin.html'}),
	url(r'^signout/$', userena_views.signout, name='userena_signout'),

	# View profiles
    url(r'^(?P<username>(?!signout|signup|signin)[\.\w]+)/$', userena_views.profile_detail, name='userena_profile_detail'),
)