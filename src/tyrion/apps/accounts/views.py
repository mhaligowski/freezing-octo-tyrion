from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect, render

from userena import views as userena_views

import forms
import utils

def signin(request, redirect_field_name=REDIRECT_FIELD_NAME, **kwargs):
	if request.method == "GET" and \
		settings.USERENA_SIGNIN_REDIRECT_IF_AUTHENTICATED and \
		request.user.is_authenticated():
		redirect_to = userena_views.signin_redirect(request.REQUEST.get(redirect_field_name), request.user)
		return redirect(redirect_to)
	else:
		return userena_views.signin(request, redirect_field_name = redirect_field_name, **kwargs)

def activate(request, activation_key, **kwargs):
    # check whether the activation key exists
    try:
        utils.check_user_activation(activation_key)
    except utils.ActivationError:
        # if activation key does not exist
        return render(request, 'activate_fail.html')

    if request.method == "GET":
        # generate the activation form
        form = forms.ActivationForm()
        return render(request, 'activate.html', { 'form': form })
    elif request.method == "POST":
        # activate and set new password
        form = forms.ActivationForm(request.POST) 

        if form.is_valid():
            utils.activate_user(activation_key, form.cleaned_data["password1"])

            # redirect to signin page
            return redirect('/accounts/signin') 
