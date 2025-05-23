"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 4.2.20.

For more information on this file, see:
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import mimetypes
import os
import socket
from pathlib import Path

from decouple import config
from django.utils.translation import gettext_lazy as _

# ---------------------------------------------------------------------
# 1) Basic Settings & Environment Variables
# ---------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Postgres environment variables (configure these in your .env file)
POSTGRES_NAME = config('POSTGRES_NAME', default='postgres')
POSTGRES_USER = config('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD', default='postgres')
POSTGRES_HOST = config('POSTGRES_HOST', default='localhost')
POSTGRES_PORT = config('POSTGRES_PORT', default='5432')

# Example: environment to distinguish dev/prod/test
ENVIRONMENT = config('ENVIRONMENT', default='development')
# Example: token expiry (OAuth?), define a default if needed
TOKEN_EXPIRE_S = config('TOKEN_EXPIRE_S', default=3600, cast=int)

# Security
SECRET_KEY = config('SECRET_KEY', default='django-insecure-p_9a^#7#2ooeih1&&2(j96fl$p9p6tyd)jk3q9-7q%0=@az*9l')
DEBUG = config('DEBUG', default=True, cast=bool)

# You should set ALLOWED_HOSTS in production
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

print(f"[INFO] ENVIRONMENT={ENVIRONMENT}, DEBUG={DEBUG}, ALLOWED_HOSTS={ALLOWED_HOSTS}")
print(f"[DB INFO] POSTGRES_HOST={POSTGRES_HOST}, POSTGRES_PORT={POSTGRES_PORT}")
print(f"[DB INFO] POSTGRES_NAME={POSTGRES_NAME}, POSTGRES_USER={POSTGRES_USER}")
print(f"[DB INFO] POSTGRES_PASSWORD={POSTGRES_PASSWORD}")

# ---------------------------------------------------------------------
# 2) Applications & Middleware
# ---------------------------------------------------------------------
INSTALLED_APPS = [
    # 'admin_volt.apps.AdminVoltConfig',
    # 'django_json_widget',
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.gis",
    'oauth2_provider',
    'solo',
    'leaflet',

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'django_extensions',
    'django_filters',
    'django_apscheduler',

    # Custom apps
    'config.apps.ConfigConfig',
    'skudra.apps.SkudraConfig',
]

MIDDLEWARE = [
    # Must go before CommonMiddleware if using django-cors-headers
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGIN_REDIRECT_URL = "/api/user/"
# LOGOUT_REDIRECT_URL = "/api/logout/"

# Add debug toolbar only if DEBUG or ENVIRONMENT is "test"
if DEBUG or ENVIRONMENT == 'test':
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

    # Set up internal IPs for the debug toolbar
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', 'localhost']
    # INTERNAL_IPS = type(str('c'), (), {'__contains__': lambda *a: True})()
    print('[INFO] internal_ips', INTERNAL_IPS)

    # Some systems need this to ensure debug toolbar assets load properly
    mimetypes.add_type("application/javascript", ".js", True)

    print("[INFO] Debug Toolbar enabled")

# ---------------------------------------------------------------------
# 3) URL & WSGI Config
# ---------------------------------------------------------------------
ROOT_URLCONF = 'setup.urls'
WSGI_APPLICATION = 'setup.wsgi.application'

# ---------------------------------------------------------------------
# 4) Database Configuration
# ---------------------------------------------------------------------
DATABASES = {
    'default': {
        # If you need PostGIS, ensure you have 'django.contrib.gis' in INSTALLED_APPS
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': POSTGRES_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
        'OPTIONS': {
            'options': f'-c search_path={POSTGRES_NAME},public'
        },
    }
}

# ---------------------------------------------------------------------
# 5) Templates
# ---------------------------------------------------------------------
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'dist'), TEMPLATES_DIR],
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

# ---------------------------------------------------------------------
# 6) Authentication & Password Validation
# ---------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------------------------------------------------
# 7) Internationalization
# ---------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('lv', 'Latviešu'),
    ('ru', 'Русский'),
    ('ro', 'Română'),
]

# If you store translations in a custom locale folder
LOCALE_PATHS = [os.path.join(BASE_DIR, '..', 'locale')]
print(f"[INFO] LOCALE_PATHS={LOCALE_PATHS}")

# ---------------------------------------------------------------------
# 8) Static & Media Files
# ---------------------------------------------------------------------
# Note: Adjust paths as needed for your environment
STATIC_URL = '/static/'

# Example layout for static files (collected in production)
STATIC_ROOT = os.path.join(BASE_DIR, 'public')

# Additional dirs from which Django will serve static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist'),
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static', 'static'),
]


if os.name == 'nt':
    os.environ['GDAL_DATA'] = r"env\Lib\site-packages\osgeo\data\gdal"
    os.environ['PROJ_LIB'] = r"env\Lib\site-packages\osgeo\data\proj"
    os.environ['PATH'] = r"env\Lib\site-packages\osgeo;" + os.environ['PATH']
    GDAL_LIBRARY_PATH = r'env\Lib\site-packages\osgeo\gdal.dll'
    

# Media files
MEDIA_URL = '/api/media/'
if os.name == 'nt':
    # Windows
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "..", "storage")
else:
    # Linux / Other
    MEDIA_ROOT = "/storage/"

print(f"[INFO] MEDIA_ROOT={MEDIA_ROOT}, STATIC_ROOT={STATIC_ROOT}")

# ---------------------------------------------------------------------
# 9) Django REST Framework Configuration
# ---------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        # 'rest_framework_datatables.renderers.DatatablesRenderer',
        # 'rest_framework_csv.renderers.CSVRenderer',
        # 'drf_excel.renderers.XLSXRenderer'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'django.middleware.csrf.CsrfViewMiddleware',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'RUNIS_API.paging.CustomResultsSetPagination',  # If this is your custom pagination
    # 'PAGE_SIZE': 50,
    'DATETIME_FORMAT': "%Y-%m-%dT%H:%M:%S",
}

# ---------------------------------------------------------------------
# 10) OAuth2 / Token Settings (If Using django-oauth-toolkit)
# ---------------------------------------------------------------------
OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups',
        'userinfo': 'Access to user info',
    },
    'ACCESS_TOKEN_EXPIRE_SECONDS': TOKEN_EXPIRE_S,  # e.g., 3600
}
print(f"[INFO] TOKEN_EXPIRE_S={TOKEN_EXPIRE_S}")

# ---------------------------------------------------------------------
# 11) Default Primary Key Field
# ---------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
