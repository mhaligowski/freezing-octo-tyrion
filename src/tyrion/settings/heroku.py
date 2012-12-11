#-*- coding: utf-8 -*-

from tyrion.settings.core import *

import os
import os.path

DEBUG = True

# create the tmp dir
(head, tail) = os.path.split(__file__)
for i in range(3): (head, tail) = os.path.split(head)

import dj_database_url
DATABASES["default"] = dj_database_url.config()

# installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    'django.contrib.admin',
)

# Userena configuration
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# static files
STATICFILES_DIRS = (
	os.path.join(head, 'www'),
)
