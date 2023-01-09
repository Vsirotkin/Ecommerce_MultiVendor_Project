"""
Django settings for Ecommerce_MultiVendor_Project project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s3f)a*k=f63mgfn3vx6s^9f3ha^8mp%e(5m2go$%jufk4#3xs7'

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

    # own
    'apps.core.apps.CoreConfig',
    'apps.vendor.apps.VendorConfig',
    'apps.product.apps.ProductConfig',
    'apps.cart.apps.CartConfig',
    'apps.order.apps.OrderConfig',
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

ROOT_URLCONF = 'Ecommerce_MultiVendor_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # own
                'apps.product.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'Ecommerce_MultiVendor_Project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static/'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
LOGIN_URL = 'vendor:login'
LOGIN_REDIRECT_URL = 'vendor:vendor_admin'
LOGOUT_REDIRECT_URL = 'core:frontpage'

# Cookie
SESSION_COOKIE_AGE = 86400  # 24 hours

# Cart Session
CART_SESSION_ID = 'cart'

# Stripe Payment
STRIPE_PUB_KEY = 'pk_test_51MD2CBCHAGEoR9VCJgBOPXd9VXVIBEAoM3ZMeu4MrdXwjgNgfK0k2Db1NOeTX3zgaAkp4450bt04thgnUuz5Yfpv002GC7maUD'
STRIPE_SECRET_KEY = 'sk_test_51MD2CBCHAGEoR9VCuwzzcRyOsi6dIdNwoDoyVYkuOOAqZv9IYzuXsICqb9DsXo2LkHxfAEAxbKZjLLapof026Ui700176vOCfM'

"""
# EMAIL MAILJET
# EMAIL_BACKEND = 'django_mailjet.backends.MailjetBackend'


# ANYMAIL = {
#     "MAILGUN_API_KEY": "0f351d5ddda56ac8549e9083fea04931",
#     "MAILGUN_SENDER_DOMAIN": "in-v3.mailjet.com",
# }
# EMAIL_PORT = 587,
# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# DEFAULT_FROM_EMAIL = "vsirotkin15@gmail.com"



This call sends a message to the given recipient with vars and custom vars.
from mailjet_rest import Client
import os
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
		{
			"From": {
				"Email": "vsirotkin15@gmail.com",
				"Name": "Vik"
			},
			"To": [
				{
					"Email": "passenger1@example.com",
					"Name": "passenger 1"
				}
			],
			"TemplateID": 4424467,
			"TemplateLanguage": True,
			"Subject": "test",
			"Variables": {}
		}
	]
}
result = mailjet.send.create(data=data)
print result.status_code
print result.json()



EMAIL_HOST = 'in-v3.mailjet.com'
MAILJET_API_KEY = "0f351d5ddda56ac8549e9083fea04931"
MAILJET_API_SECRET = "56a79e72169275a4adccb9211573330d"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = 30
DEFAULT_EMAIL_FROM = 'my_shop <admin@e.com>'

import mailjet

mailjet_api = mailjet.Api(api_key='0f351d5ddda56ac8549e9083fea04931', secret_key='56a79e72169275a4adccb9211573330d')
account_info = mailjet_api.user.infos()
"""
