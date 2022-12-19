web: python manage.py collectstatic --no-imput \
    && python manage.py migrate \
    && gunicorn bandkamp.wsgi --log-level debug
