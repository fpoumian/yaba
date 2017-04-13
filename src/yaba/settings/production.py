import os

from .base import *

DEBUG = False

# Allowed Hosts
ALLOWED_HOSTS = [
    'ec2-54-175-168-118.compute-1.amazonaws.com'
]

# Production Database (Amazon RDS)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}

# AWS
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

INSTALLED_APPS += ('storages',)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# S3 Static File Storage
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'yaba.storages.static_storage.StaticStorage'
AWS_STORAGE_BUCKET_NAME = 'fernandocodes'
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
