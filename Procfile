release: python manage.py migrate
web: gunicorn dsbj.wsgi --port $PORT --host 0.0.0.0