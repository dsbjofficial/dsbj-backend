release: python manage.py migrate
web: gunicorn dsbj.wsgi -b 0.0.0.0:$PORT