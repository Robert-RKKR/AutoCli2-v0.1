# Python - libraries import:
from pathlib import Path
import os

# Jazzmin - settings import:
from .jazzmin import GLOBAL_JAZZMIN_SETTINGS

# Celery - import:
from kombu import Exchange
from kombu import Queue

# Basis application data.
# BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = os.environ.get("SECRET_KEY")
# DEBUG = int(os.environ.get("DEBUG", default=0))
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
# NOTIFICATION_DEBUG = int(os.environ.get("NOTIFICATION_DEBUG", default=0))
# LOGGER_DEBUG = os.environ.get("LOGGER_DEBUG").split(" ")
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-#8$u0eijwv%8v$fm!7z62ogxavmv-prab76=f2mg$63d&6kngj'
DEBUG = True
ALLOWED_HOSTS = []
NOTIFICATION_DEBUG = True
LOGGER_DEBUG = True

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

    # Celery and channels:
    'django_celery_beat',
    'channels',

    # Django rest framework:
    # 'rest_framework_simplejwt.token_blacklist',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_framework',
    'django_filters',
    'drf_yasg',

    # AutoCli2 applications:
    'a_test.apps.ATestConfig', # Temporary.
    'notification.apps.NotificationConfig',
    'management.apps.ManagementConfig',
    'connector.apps.ConnectorConfig',
    'inventory.apps.InventoryConfig',
    'executor.apps.ExecutorConfig',

    # AutoCli2 init application:
    'app_initiator.apps.AppInitiatorConfig',
]

# Main URL file:
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
ASGI_APPLICATION = 'autocli2.asgi.application'

# Celery configuration:
# BROKER_URL = 'amqp://guest:guest@rabbitmq-server:5672//'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_IGNORE_RESULT = True

# Celery task queues and routes:
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('executor', Exchange('executor'), routing_key='executor'),
    Queue('notification', Exchange('notification'), routing_key='notification'),
)
CELERY_ROUTES = {
    'my_taskA': {'queue': 'executor', 'routing_key': 'executor'},
    'my_taskB': {'queue': 'notification', 'routing_key': 'notification'},
}

# Channels configuration:
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.pubsub.RedisPubSubChannelLayer',
        'CONFIG': {
            'hosts': ['redis://127.0.0.1:6379'],
        },
    },
}

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
JAZZMIN_SETTINGS = GLOBAL_JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
}

# Rest Framework API:
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'autocli2.base.api.base_exception_handler.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
}

# Database:
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
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
USE_L10N = True

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
