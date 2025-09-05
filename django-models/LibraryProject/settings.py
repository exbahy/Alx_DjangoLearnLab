# في ملف LibraryProject/settings.py (داخل مجلد LibraryProject الرئيسي للمشروع)

from pathlib import Path
import os # تأكد من وجود هذا السطر
import sys # <<<<<<<<<<<<<<<<< أضف هذا السطر هنا <<<<<<<<<<<<<<<<<

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # هذا السطر يفترض أنه موجود

# أضف مجلد المشروع الرئيسي (الذي يحتوي على manage.py والتطبيقات) إلى sys.path
# هذا يضمن أن Django يستطيع إيجاد 'relationship_app'
sys.path.append(str(BASE_DIR)) # <<<<<<<<<<<<<<<<< أضف هذا السطر هنا <<<<<<<<<<<<<<<<<

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yl&soelv$sg&u6w@w(0s9z0a+6s8b_5(6v1d*2a4+v2k-z' # مثال

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # تطبيقاتك هنا
    'relationship_app.apps.RelationshipAppConfig', # <<<<<<<<<<<<<<<<< أضف هذا السطر هنا <<<<<<<<<<<<<<<<<
    # إذا كان لديك تطبيق bookshelf من مهمة سابقة، لا تضفه في هذا المشروع الجديد لتجنب التعقيد
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

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# (استخدم SQLite للدعم الافتراضي السهل، أو MySQL إذا أردت)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # استخدام SQLite لتبسيط الأمور
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # إذا كنت تريد MySQL، قم بتغيير هذا الجزء واضبطه بدقة
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mydatabase',
    #     'USER': 'mydatabaseuser',
    #     'PASSWORD': 'mypassword',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'