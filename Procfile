web: cd django_web_app && gunicorn django_web_app.wsgi:application
release: cd django_web_app && python manage.py migrate && python manage.py collectstatic --noinput
