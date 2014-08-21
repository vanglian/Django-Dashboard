"""
Django settings for SocialIQ project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#for putting apps in one folder ~VL
#PROJECT_ROOT = os.path.dirname(__file__)
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6s)=ro$=%zz7d$&@dms!cz$h-s=$6(erx*_!5kho$+30q3hjgp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'import_export',
	'textanalytics',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SocialIQ.urls'

WSGI_APPLICATION = 'SocialIQ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC+5:30'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_URL = '/plugins/'
STATIC_URL = '/static/'
'''STATICFILES_DIRS = (
    "/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/static/",
	"ajax","plugins",
	"/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/ajax/",
	"/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/static/ajax/",
	"/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/static/plugins/",
	"/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/css/",
	"/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/fonts/",
    
)
'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static/plugins"),
    '/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/plugins/',
    '/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/css/',
    '/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/fonts/',
    '/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/js/',
    '/Users/Lian/Dropbox/inrev/Research/vizualization/SocialIQ/img/',
)