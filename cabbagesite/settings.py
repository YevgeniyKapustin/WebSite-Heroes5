import os
from pathlib import Path
from . import confidential

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = confidential.SECRET_KEY

DEBUG = confidential.DEBUG

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'reports.apps.ReportsConfig',
    'stats.apps.StatsConfig',
    'download_game.apps.DownloadGameConfig',
    'kateusta.apps.KateustaConfig',
    'guides.apps.GuidesConfig',
    'mods_and_maps.apps.ModsAndMapsConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'cabbagesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

DATABASES = confidential.DATABASES

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'cabbagesite/static')
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    "127.0.0.1",
]

game_link = 'https://drive.google.com/file/d/1Pf3heEC8OwC-q4wPXThmASO0trSwcWVs/view?usp=sharing'
game_image = '/media/game.png'

kateusta_link = 'https://disk.yandex.ru/d/QeUEhYAX7TCYoQ'
kateusta_version = 1.14

online_link = 'https://drive.google.com/file/d/1Pf3heEC8OwC-q4wPXThmASO0trSwcWVs/view?usp=sharing'
online_image = '/media/online.png'
