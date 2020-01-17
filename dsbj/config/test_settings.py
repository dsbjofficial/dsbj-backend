from .common_settings import Common


class Test(Common):
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
    REST_FRAMEWORK = {**super().REST_FRAMEWORK, 'TEST_REQUEST_DEFAULT_FORMAT': 'json'}
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
