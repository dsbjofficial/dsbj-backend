import os
import dj_database_url
from .common_settings import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
# Site
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn",)
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# AWS S3 Storage
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += ('storages',)
AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = os.getenv("DJANGO_AWS_DOMAIN")
AWS_DEFAULT_ACL = None
AWS_AUTO_CREATE_BUCKET = True
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
}
# S3 Static Files
AWS_STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
STATICFILES_STORAGE = 'dsbj.storage_backends.StaticStorage'
# S3 Public Media Files
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'dsbj.storage_backends.PublicMediaStorage'
# S3 Private Media Files
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_MEDIA_FILE_STORAGE = 'dsbj.storage_backends.PrivateMediaStorage'

# Database
DATABASES = {
    'default': dj_database_url.config(ssl_require=True)
}
# Heroku-specific configuration
if "DYNO" in os.environ:
    import django_heroku
    django_heroku.settings(locals(), databases=False, test_runner=False, allowed_hosts=False, secret_key=False,
                           staticfiles=False)
