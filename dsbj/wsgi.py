"""
WSGI config for dsbj project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior dsbj directory.
app_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)
sys.path.append(os.path.join(app_path, "dsbj"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.production_settings")

application = get_wsgi_application()
