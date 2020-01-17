import os
from .common_settings import *

DEBUG = True
os.environ.setdefault("SECRET_KEY", "(cwvjff3d+*db30ym7cfz(sf43^bmves2qb67w%47_sf734qa*")
SECRET_KEY = os.getenv("SECRET_KEY")

# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
