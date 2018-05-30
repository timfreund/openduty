"""
Django settings for openduty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType
djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", False)

ALLOWED_HOSTS = ['*']

BROKER_URL = 'django://'

LOGIN_URL = '/login/'

PROFILE_MODULE = 'openduty.UserProfile'


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'kombu.transport.django',
    'openduty',
    'openduty.templatetags',
    'schedule',
    'djcelery',
    'notification',
    'django_tables2',
    'django_tables2_simplefilter',
    'bootstrap3',
    "django_twilio"
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + 'templates',
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'openduty.urls'

WSGI_APPLICATION = 'openduty.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIRST_DAY_OF_WEEK = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 10
}

PAGINATION_DEFAULT_PAGINATION = 20 # The default amount of items to show on a page if no number is specified.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT =  os.path.realpath(os.path.dirname(__file__))+"/static/"
STATICFILES_DIRS = (
    os.path.realpath(os.path.dirname(__file__))+'/static_schedule/',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

AUTH_PROFILE_MODULE = 'openduty.UserProfile'

BASE_URL = os.environ['BASE_URL']

# External Service Settings (Start)

EMAIL_SETTINGS = {
   'user': os.environ.get('EMAIL_SETTINGS_USER'),
   'password': os.environ.get('EMAIL_SETTINGS_PASSWORD')
}

HIPCHAT_SETTINGS = {

}

PROWL_SETTINGS = {

}

SLACK_SETTINGS = {
    'apikey': os.environ.get('SLACK_SETTINGS_APIKEY')
}

TWILIO_SETTINGS = {
    'SID': os.environ.get('TWILIO_SETTINGS_SID'),
    'token': os.environ.get('TWILIO_SETTINGS_TOKEN'),
    'phone_number': os.environ.get('TWILIO_SETTINGS_PHONE_NUMBER'),
    'sms_number': os.environ.get('TWILIO_SETTINGS_SMS_NUMBER'),
    'twiml_url': os.environ.get('TWILIO_SETTINGS_TWIM_URL')
}

if os.environ.has_key('XMPP_SETTINGS_USER'):
    XMPP_SETTINGS = {
        'user': os.environ['XMPP_SETTINGS_USER'],
        'password': os.environ['XMPP_SETTINGS_PASSWORD'],
        'server': os.environ['XMPP_SETTINGS_SERVER'],
        'port': int(os.environ['XMPP_SETTINGS_PORT'])
    }


# External Service Settings (End)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASES_DEFAULT_NAME'],
        'USER': os.environ['DATABASES_DEFAULT_USER'],
        'PASSWORD': os.environ['DATABASES_DEFAULT_PASSWORD'],
        'HOST': os.environ['DATABASES_DEFAULT_HOST'],
        'PORT': int(os.environ['DATABASES_DEFAULT_PORT'])
    }
}
TWILIO_ACCOUNT_SID = TWILIO_SETTINGS.get("SID", "disabled")
TWILIO_AUTH_TOKEN = TWILIO_SETTINGS.get("token", "disabled")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

AUTH_LDAP_SERVER_URI = os.environ.get("AUTH_LDAP_SERVER_URI", None)
AUTH_LDAP_BIND_DN = os.environ.get("AUTH_LDAP_BIND_DN", None)
AUTH_LDAP_BIND_PASSWORD = os.environ.get("AUTH_LDAP_BIND_PASSWORD", None)
AUTH_LDAP_START_TLS = os.environ.get("AUTH_LDAP_START_TLS", 'False').upper() == 'TRUE'
AUTH_LDAP_MIRROR_GROUPS = os.environ.get("AUTH_LDAP_MIRROR_GROUPS", 'False').upper() == 'TRUE'
AUTH_LDAP_GROUP_BASE = os.environ.get("AUTH_LDAP_GROUP_BASE", None)
AUTH_LDAP_GROUP_FILTER = os.environ.get("AUTH_LDAP_GROUP_FILTER", None)
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(AUTH_LDAP_GROUP_BASE, ldap.SCOPE_SUBTREE, AUTH_LDAP_GROUP_FILTER)
AUTH_LDAP_USER_BASE = os.environ.get("AUTH_LDAP_USER_BASE", None)
AUTH_LDAP_USER_FILTER = os.environ.get("AUTH_LDAP_USER_FILTER", None)
AUTH_LDAP_USER_SEARCH = LDAPSearch(AUTH_LDAP_USER_BASE, ldap.SCOPE_SUBTREE, AUTH_LDAP_USER_FILTER)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

if AUTH_LDAP_SERVER_URI:
    AUTHENTICATION_BACKENDS.insert(0, 'django_auth_ldap.backend.LDAPBackend')
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',)

import sys
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_sqlite.db',
        }
    }


    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
    )
