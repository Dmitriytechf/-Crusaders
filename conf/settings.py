from pathlib import Path
import os
import environ


env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
env_file = BASE_DIR / '.env'

environ.Env.read_env(env_file)

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = [
    'jazzmin',
    'captcha',
    'crispy_bootstrap4',
    'crispy_forms',
    
    # apps
    'homepage',
    'questions',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'


# База данных
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'OPTIONS': {
            'client_encoding': 'UTF8',
        }
    }
}

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


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_CHARSET = 'utf-8'

# Настройки капчи
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge' математические операции
CAPTCHA_LENGTH = 6  # Длина символов
CAPTCHA_FONT_SIZE = 52  # Размер шрифта
CAPTCHA_IMAGE_SIZE = (400, 150)  # Размер изображения
CAPTCHA_BACKGROUND_COLOR = '#ffffff'  # Цвет фона
CAPTCHA_FOREGROUND_COLOR = '#001100'  # Цвет текста
CAPTCHA_TIMEOUT = 5 # Время жизни капчи в минутах
