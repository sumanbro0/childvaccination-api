web: celery -A core worker --loglevel=info -P solo & celery -A core beat --loglevel=info & python manage.py migrate && gunicorn core.wsgi --log-file -
