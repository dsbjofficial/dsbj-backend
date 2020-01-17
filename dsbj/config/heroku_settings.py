import os
import dj_database_url
import django_heroku
from .common_settings import *


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
# Site
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn", )
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': dj_database_url.config(ssl_require=True)
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += ('storages',)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

django_heroku.settings(locals(), databases=False, test_runner=False, allowed_hosts=False, secret_key=False,
                       staticfiles=False)
