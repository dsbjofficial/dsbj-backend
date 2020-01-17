from .common_settings import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'

# Testing
INSTALLED_APPS = INSTALLED_APPS
INSTALLED_APPS += ('pytest_django',)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    BASE_DIR,
    '-s',
    '--nologcapture',
    '--with-coverage',
    '--cover-package=dsbj',
    '--exclude-dir=dsbj/config',
]

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
