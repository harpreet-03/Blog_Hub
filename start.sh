#!/bin/bash

# Railway deployment script
echo "🚀 Starting Django deployment..."

# Set production environment
export RAILWAY_ENVIRONMENT=production
export DEBUG=False

# Change to django_web_app directory
cd django_web_app

# Generate and run migrations
echo "📝 Generating and running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Start gunicorn using python module
echo "🌐 Starting server..."
python -m gunicorn django_web_app.wsgi:application --bind 0.0.0.0:$PORT
