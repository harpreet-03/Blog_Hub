#!/bin/bash

# Railway deployment script
echo "🚀 Starting Django deployment..."

# Change to django_web_app directory
cd django_web_app

# Run migrations
echo "📝 Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Start gunicorn
echo "🌐 Starting server..."
gunicorn django_web_app.wsgi:application --bind 0.0.0.0:$PORT
