"""
Django settings for caricaturas project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os
#import psycopg2
#import dj_database_url
import datetime
from datetime import timedelta
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r+ra2!l8*$2lb7p8kgt1&vlvtr_4q$)up(((6w#-=@m4w&s*t2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'dibujos',
    's3_folder_storage',
    #'usuarios',
    #'storages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'caricaturas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.path.join(os.path.abspath(__file__)),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSOR = (
    'django.core.context_processors.csrf',
)

WSGI_APPLICATION = 'caricaturas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default' : {
    'ENGINE' : 'django.db.backends.mysql',
    'NAME' : 'heroku_890a2281d54fb25',
    'USER' : 'ba53bc3c2a0b70',
    'PASSWORD' : '00d224fb',
    'HOST' : 'us-cdbr-iron-east-02.cleardb.net',
    'PORT' : '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

STATIC_URL = '/static/'

MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL = '/media/'
#STATICFILES_DIRS = (
 #   os.path.join(BASE_DIR, 'static'),
 #   

#)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



CORS_ORIGIN_ALLOW_ALL = True

# Permisos de acceso de los servidores. No funciona, uso la linea de arriba
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1',
    '127.0.0.1:8000',
    'lit-woodland-9635',
    'lit-woodland-9635.herokuapp.com',
)

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'OPTIONS'
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)

CSRF_COOKIE_SECURE = True
#Backends:
#AUTHENTICATION_BACKENDS = (
 #   'usuarios.backends.EmailBackend',
#)




# Configuracion AWS
#AWS_QUERYSTRING_AUTH = False
#AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY')
#AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_KEY')
#AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

#tenyrs = datetime.datetime.now() + timedelta(days=365*10)
#AWS_HEADERS = {
#    'Expires' : tenyrs.strftime('%a, %d %b %Y 20:00:00 GMT')
#}
#STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
#STATIC_URL = 'http://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
#STATIC_S3_PATH = 'static/'
