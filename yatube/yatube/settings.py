"""
Django settings for yatube project.

Generated by 'django-admin startproject' using Django 2.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y#+#ot(2$07bag5os(0_)7r)+(!x8te6rre*&$4(!vw&9t6ohz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_FAILURE_VIEW = 'core.views.csrf_failure'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
    'testserver',
]


# Application definition

INSTALLED_APPS = [
    'about.apps.AboutConfig',  # Добавили приложение about
    'core.apps.CoreConfig',  # Добавили приложение core
    'users.apps.UsersConfig',  # Добавили приложение users
    'posts.apps.PostsConfig',  # Добавили приложение posts
    'django.contrib.admin',
    'django.contrib.auth',  # Приложение для регистрации и авторизации пользователей
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
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

ROOT_URLCONF = 'yatube.urls'

# Путь к директории с шаблонами вынесен в переменную:
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # Добавлено: Искать шаблоны на уровне проекта
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Добавлен контекст-процессор
                'core.context_processors.year.year',
            ],
        },
    },
]

WSGI_APPLICATION = 'yatube.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# Добавили путь до статики
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'posts:index'
# LOGOUT_REDIRECT_URL = 'posts:index'

# Эмулятор почты
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# Директорию, где хранятся письма
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
