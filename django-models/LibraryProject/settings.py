# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\settings.py

from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR هو الآن C:\Users\user\Alx_DjangoLearnLab\django-models
# هذا السطر مهم جداً لأنه يحدد جذر المشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# هذا السطر مهم جداً لجعل Django يرى التطبيقات مباشرة (مثل relationship_app)
# بإضافة BASE_DIR إلى sys.path، فإننا نضمن أن بايثون يمكنها العثور على أي تطبيق
# موجود مباشرة تحت مجلد django-models (حيث يوجد manage.py)
sys.path.append(str(BASE_DIR)) # <<<<<<<<<<<<<<<<< أضف هذا السطر هنا <<<<<<<<<<<<<<<<<


# SECURITY WARNING: keep the secret key used in production secret!
# هذا المفتاح السري مهم جداً، Django يولده تلقائياً عند إنشاء المشروع.
# لا يجب أن يتم مشاركته في البيئات الإنتاجية.
SECRET_KEY = 'django-insecure-yl&soelv$sg&u6w@w(0s9z0a+6s8b_5(6v1d*2a4+v2k-z' # مثال لمفتاح سري، سيكون لديك واحد خاص بك

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True يظهر لك صفحات الأخطاء التفصيلية، وهو مثالي للتطوير.
# يجب أن يكون False في بيئات الإنتاج.
DEBUG = True

# ALLOWED_HOSTS تحدد عناوين الـ Host التي يُسمح لها بخدمة مشروعك.
# [] تعني أي Host (للتطوير)، لكن في الإنتاج يجب تحديد العناوين بالضبط.
ALLOWED_HOSTS = []


# Application definition (تعريف التطبيقات)

# INSTALLED_APPS هي قائمة بجميع تطبيقات Django التي يستخدمها مشروعك.
# يجب إضافة أي تطبيق تقوم بإنشائه هنا.
INSTALLED_APPS = [
    'django.contrib.admin',        # لوحة التحكم الإدارية الافتراضية
    'django.contrib.auth',         # نظام المصادقة (Authentication)
    'django.contrib.contenttypes', # نظام لأنواع المحتوى (Content Types)
    'django.contrib.sessions',     # نظام إدارة الجلسات (Sessions)
    'django.contrib.messages',     # نظام الرسائل (Messages framework)
    'django.contrib.staticfiles',  # إدارة الملفات الثابتة (CSS, JS, Images)
    # تطبيقاتك المخصصة هنا
    'relationship_app.apps.RelationshipAppConfig', # <<<<<<<<<<<<<<<<< أضف هذا السطر هنا <<<<<<<<<<<<<<<<<
    # لو كان لديك تطبيقات أخرى مثل 'bookshelf' من مهمة سابقة، لا تضعها هنا في هذا المشروع الجديد
    # إلا إذا كانت جزءاً من متطلبات هذه المهمة بالذات.
]

# MIDDLEWARE هي قائمة بـ "البرمجيات الوسيطة" التي تعالج الطلبات والاستجابات.
# تؤدي وظائف مثل الأمان، إدارة الجلسات، حماية CSRF، إلخ.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF يحدد ملف urls.py الرئيسي للمشروع.
ROOT_URLCONF = 'LibraryProject.urls'

# TEMPLATES هي إعدادات نظام القوالب (Template system) الخاص بـ Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # هنا يمكن تحديد مسارات إضافية للقوالب
        'APP_DIRS': True, # Django سيبحث عن قوالب داخل مجلدات 'templates' في كل تطبيق
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

# WSGI_APPLICATION هو نقطة دخول تطبيقك لخوادم الويب المتوافقة مع WSGI.
WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database (إعدادات قاعدة البيانات)
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# نستخدم SQLite هنا لأنه الأسهل للتطوير ولا يتطلب تثبيت سيرفر خارجي.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # تحديد محرك SQLite
        'NAME': BASE_DIR / 'db.sqlite3', # اسم ملف قاعدة البيانات
    }
    # إذا كنت تريد استخدام MySQL، قم بإلغاء التعليق عن الجزء التالي وتعديله بدقة:
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mydatabase',        # اسم قاعدة البيانات في MySQL
    #     'USER': 'mydatabaseuser',    # اسم المستخدم في MySQL
    #     'PASSWORD': 'mypassword',    # كلمة المرور للمستخدم في MySQL
    #     'HOST': 'localhost',         # عنوان سيرفر MySQL
    #     'PORT': '3306',              # منفذ سيرفر MySQL الافتراضي
    # }
}


# Password validation (قواعد التحقق من كلمة المرور)
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
# هذه القواعد تُطبق عند إنشاء أو تغيير كلمة مرور المستخدمين.
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


# Internationalization (تدويل التطبيق - اللغات والمنطقة الزمنية)
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us' # اللغة الافتراضية

TIME_ZONE = 'UTC' # المنطقة الزمنية الافتراضية

USE_I18N = True # تفعيل دعم التدويل

USE_TZ = True # تفعيل دعم المناطق الزمنية


# Static files (CSS, JavaScript, Images) (الملفات الثابتة)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# هنا يتم تحديد مكان ملفات CSS, JavaScript, الصور الخاصة بتطبيقك.
STATIC_URL = 'static/'

# Default primary key field type (نوع حقل المفتاح الأساسي الافتراضي)
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
# يحدد نوع حقل المفتاح الأساسي الافتراضي للموديلز.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'