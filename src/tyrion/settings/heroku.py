#-*- coding: utf-8 -*-

from tyrion.settings.core import *

import os
import os.path

DEBUG = False
ENABLE_ADMIN = True

# secret key is taken from the env
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# create the tmp dir
(head, tail) = os.path.split(__file__)
for i in range(3): (head, tail) = os.path.split(head)

import dj_database_url
DATABASES["default"] = dj_database_url.config()

# installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    'django.contrib.admin',
)

# email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_USE_TLS = False

# static files
STATIC_ROOT = os.path.join(head, 'static')

STATICFILES_DIRS = (
	os.path.join(head, 'www'),
)
