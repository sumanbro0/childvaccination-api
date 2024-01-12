web: python manage.py migrate && python manage.py collectstatic && gunicorn core.wsgi --log-file -
worker: celery -A core worker --loglevel=info --uid 1000 
beat: celery -A core beat --loglevel=info