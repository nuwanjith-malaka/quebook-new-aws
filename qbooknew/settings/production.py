from .common import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['quebooknew2.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quebook',
        'USER': 'malaka',
        'PASSWORD': 'malaka1999625',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


LOGIN_REDIRECT_URL = 'http://quebooknew2.herokuapp.com/'
LOGIN_URL = 'http://quebooknew2.herokuapp.com/login/'