from .base import *

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "poumian-yaba"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yaba',
        'USER' : 'fpoumian',
        'PASSWORD' : 'ferporo3524!',
        'HOST' : 'yaba.calwnpkeoi9o.us-east-1.rds.amazonaws.com',
        'PORT' : '5432',
    }
}