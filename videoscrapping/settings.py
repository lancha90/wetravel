"""
Django settings for videoscrapping project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# Parse database configuration from $DATABASE_URL
import dj_database_url

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

ADMINS = (
    ('Diego Mauricio Herrera Alzate', 'diegomao627@gmail.com'),
)

MANAGERS = ADMINS

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,'static'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zlij!re5yl0c!af$l&kju600nul%$9zozlmfh4z^&$s*ygl7vy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True




TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,'html'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'video',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'videoscrapping.urls'

WSGI_APPLICATION = 'videoscrapping.wsgi.application'


# =========== HEROKU CONFIGURATION =====================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dft5233ksn262e',                      # Or path to database file if using sqlite3.
        'USER': 'dslsqdnurxetuc',                      # Not used with sqlite3.
        'PASSWORD': 'ZLQtStKjMHzSNw7Z4zn5HqcEBy',                  # Not used with sqlite3.
        'HOST': 'ec2-107-21-226-77.compute-1.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
STATIC_ROOT = 'staticfiles'
# =========== END HEROKU CONFIGURATION =====================


# =========== LOCAL CONFIGURATION =====================
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'videoscrapping',                      # Or path to database file if using sqlite3.
#        'USER': 'root',                      # Not used with sqlite3.
#        'PASSWORD': '123456',                  # Not used with sqlite3.
#        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}
#ALLOWED_HOSTS = []
#STATIC_ROOT = ''

# =========== END LOCAL CONFIGURATION =====================

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

LANGUAGE_CODE = 'es-CO'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
