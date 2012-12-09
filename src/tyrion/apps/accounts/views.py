from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect

from userena import views as userena_views

def signin(request, redirect_field_name=REDIRECT_FIELD_NAME, **kwargs):
	if request.method == "GET" and \
		settings.USERENA_SIGNIN_REDIRECT_IF_AUTHENTICATED and \
		request.user.is_authenticated():
		redirect_to = userena_views.signin_redirect(request.REQUEST.get(redirect_field_name), request.user)
		return redirect(redirect_to)
	else:
		return userena_views.signin(request, redirect_field_name = redirect_field_name, **kwargs)



