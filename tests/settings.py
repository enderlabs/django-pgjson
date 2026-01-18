# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, '..')

PROJECT_ROOT = os.path.dirname(__file__)
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE', 'test'),
        'USER': os.environ.get('PGUSER', ''),
        'PASSWORD': os.environ.get('PGPASSWORD', ''),
        'HOST': os.environ.get('PGHOST', 'localhost'),
        'PORT': os.environ.get('PGPORT', ''),
    }
}

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en'
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = ()

SECRET_KEY = 'di!n($kqa3)nd%ikad#kcjpkd^uw*h%*kj=*pm7$vbo6ir7h=l'

INSTALLED_APPS = (
    'pg_json_fields',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
