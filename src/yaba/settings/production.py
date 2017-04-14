import os

from .base import *

DEBUG = False

# Email SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_env_variable('GMAIL_SMTP_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('GMAIL_SMTP_HOST_PASSWORD')
EMAIL_PORT = 587

# Allowed Hosts
ALLOWED_HOSTS = [
    'ec2-54-175-168-118.compute-1.amazonaws.com'
]

# Production Database (Amazon RDS)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('RDS_DB_NAME'),
        'USER': get_env_variable('RDS_USERNAME'),
        'PASSWORD': get_env_variable('RDS_PASSWORD'),
        'HOST': get_env_variable('RDS_HOSTNAME'),
        'PORT': get_env_variable('RDS_PORT'),
    }
}

# AWS
AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')

# S3 Storage
INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = 'fernandocodes'
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

# S3 Static File Storage
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'yaba.storages.static_storage.StaticStorage'
STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# S3 Media Files Storage
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'yaba.storages.media_storage.MediaStorage'
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
