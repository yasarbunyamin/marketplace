from marketplace.base import INSTALLED_APPS, MIDDLEWARE  # NOQA

SECRET_KEY = 'Custom@CI123Settings'
DEBUG = False
DEBUG_TOOLBAR = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ci',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    },
}
