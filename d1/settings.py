from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# print(BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','django-insecure-mfl%ws+ck^&med--m1@4i(=ac7)$%q8sb1krb5^rq4@xp!p_)p')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG'))=="1"

ALLOWED_HOSTS=['*']
# if not DEBUG:
#     ALLOWED_HOSTS+=[os.environ.get('DJANGO_ALLOWED_HOST')]
# else:
#     ALLOWED_HOSTS = ['127.0.0.1','localhost']
# # Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    
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

ROOT_URLCONF = 'd1.urls'
LOGIN_URL= '/login/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
           
            ],
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

WSGI_APPLICATION = 'd1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES={
   "default": dj_database_url.parse('postgresql://articles_ywsv_user:3En5yPxut3tf549FAAQEGzgS894fZ7sp@dpg-cr3hdhjv2p9s73dtaeo0-a.oregon-postgres.render.com/articles_ywsv')
}
# postgresql://articles_django_user:tnoSkVWmvflW95eKEfcKphiDhySqwfSj@dpg-cr3e7iaj1k6c73dl1gc0-a.oregon-postgres.render.com/articles_django
# POSTGRES_DB = os.environ.get("POSTGRES_DB")
# POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
# POSTGRES_USER = os.environ.get("POSTGRES_USER")
# POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
# POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

# POSTGRES_READY = (
#     POSTGRES_DB is not None
#     and POSTGRES_PASSWORD is not None
#     and POSTGRES_USER is not None
#     and POSTGRES_HOST is not None
#     and POSTGRES_PORT is not None
# )

# if POSTGRES_READY:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": POSTGRES_DB,
#             "USER": POSTGRES_USER,
#             "PASSWORD": POSTGRES_PASSWORD,
#             "HOST": POSTGRES_HOST,
#             "PORT": POSTGRES_PORT,
#         }
#     }
    
    
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
