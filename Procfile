web: python manage.py migrate && gunicorn core.wsgi --log-file -
worker: celery -A core worker --loglevel=info -c 4
beat: celery -A core beat --loglevel=info