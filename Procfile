

web: celery -A core worker --loglevel=info & celery -A core beat --loglevel=info & python manage.py migrate && gunicorn core.wsgi --log-file -
