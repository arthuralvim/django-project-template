"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

from decouple import config
from dj_database_url import parse as db_url
from os.path import join
from sys import path
from unipath import Path

BASE_DIR = Path(__file__).absolute().ancestor(2)

# insert path to apps
path.insert(0, BASE_DIR.child('apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

PROJECT_NAME = '{{ project_name }}'
ALLOWED_HOSTS = ['.{{ project_name }}.com.br', ]

ADMINS = ()


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'example',
)

THIRD_PARTY_APPS = (
    'gunicorn',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///{0}/{1}'.format(BASE_DIR.child('db'), '{{ project_name }}.sqlite3'),
        cast=db_url),
}

FIXTURE_DIRS = (join(BASE_DIR.child('db'), 'fixtures'), )

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (BASE_DIR.child('locale'), )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_ROOT = config('STATIC_ROOT', default=BASE_DIR.child('staticfiles'))
STATIC_URL = config('STATIC_URL', default='/static/')
STATICFILES_DIRS = (BASE_DIR.child('static'), )

# Media files
MEDIA_ROOT = config('MEDIA_ROOT', default=BASE_DIR.child('media'))
MEDIA_URL = config('MEDIA_URL', default='/media/')


# TEMPLATE

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

# Email

SEND_EMAIL = config('SEND_EMAIL', cast=bool)
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USER = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_TLS = config('EMAIL_TLS')

if SEND_EMAIL:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = EMAIL_HOST
    EMAIL_HOST_USER = EMAIL_USER
    EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
    EMAIL_PORT = EMAIL_PORT
    EMAIL_USE_TLS = EMAIL_TLS
    SERVER_EMAIL = EMAIL_HOST_USER
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ALL OTHER KEYS
from keys import *
