web: cd django_web_app && python -m gunicorn django_web_app.wsgi:application --bind 0.0.0.0:$PORT
release: cd django_web_app && python manage.py makemigrations --noinput && python manage.py migrate && python manage.py collectstatic --noinput
