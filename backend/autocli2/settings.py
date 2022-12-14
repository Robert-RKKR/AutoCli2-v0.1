"""
Django settings for autocli2 project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# Python import:
from pathlib import Path
import os

# Jazzmin Import:
from .jazzmin import JAZZMIN_SETTINGS

# Basis application data.
# BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = os.environ.get("SECRET_KEY")
# DEBUG = int(os.environ.get("DEBUG", default=0))
# LOG_DEBUG = int(os.environ.get("DEBUG", default=0))
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-#8$u0eijwv%8v$fm!7z62ogxavmv-prab76=f2mg$63d&6kngj'
DEBUG = True
LOG_DEBUG = True
ALLOWED_HOSTS = []

# Application definition:
INSTALLED_APPS = [
    # Django Jazzmin:
    'jazzmin',
    
    # Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # AutoCli2 data apps:
    # 'data.automation.apps.AutomationConfig',
    # 'data.dataset.apps.DatasetConfig',
    'data.inventory.apps.InventoryConfig',
    # 'data.update.apps.UpdateConfig',
    # 'data.tag.apps.TagConfig',

    # AutoCli2 message apps:
    'message.notification.apps.NotificationConfig',
    # 'message.change.apps.ChangeConfig',
    # 'message.log.apps.LogConfig',

    # AutoCli2 setting app:
    # 'system.setting.apps.SettingsConfig',
]
ROOT_URLCONF = 'autocli2.urls'

# Middleware definition:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# WSGI and ASGI configuration:
WSGI_APPLICATION = 'autocli2.wsgi.application'
# ASGI_APPLICATION = 'autocli2.asgi.application'

# Celery configuration:
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Channels configuration:
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('127.0.0.1', 6379)],
#         },
#     },
# }

# Templates:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'),
            BASE_DIR.joinpath('static'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static', 
            }
        },
    },
]

# Jazzmin settings:
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
}

# Rest Framework API:
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 10,
#     'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissions',
#     ],
# }

# Database:
# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
#         "USER": os.environ.get("SQL_USER", "user"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#         "HOST": os.environ.get("SQL_HOST", "localhost"),
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation:
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization:
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files:
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath('static'),
    BASE_DIR.joinpath('media'),
]
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

# Default primary key field type:
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
