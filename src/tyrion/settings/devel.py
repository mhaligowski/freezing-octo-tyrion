#-*- coding: utf-8 -*-

from tyrion.settings.core import *

import os
import os.path

DEBUG = True
ENABLE_ADMIN = True

# secret key
SECRET_KEY = '!o_p6jcgat)o0!@*vq1xut+7uqk=#cv!rva0+ujga_+b_r@5o4'

# create the tmp dir
(head, tail) = os.path.split(__file__)
for i in range(3): (head, tail) = os.path.split(head)

db_path = os.path.join(head, 'tmp')
if not os.path.exists(db_path): os.makedirs(db_path) 

DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(db_path, 'devel.sqlite3'),                      
   }
}

INSTALLED_APPS = INSTALLED_APPS + (
    'django.contrib.admin',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = db_path

STATICFILES_DIRS = (
	os.path.join(head, 'www'),
)

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost', )
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': False,
    'TAG': 'body',
    'ENABLE_STACKTRACES' : True,
}