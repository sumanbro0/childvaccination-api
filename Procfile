web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi --log-file -
worker: celery -A core worker --loglevel=info
beat: celery -A core beat --loglevel=info