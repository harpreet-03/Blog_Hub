#!/bin/bash

echo "🚀 Setting up Django for Vercel..."

# Install dependencies
pip install -r requirements.txt

# Set up Django
cd django_web_app

# Generate migrations
python manage.py makemigrations --noinput

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

echo "✅ Django setup complete!"
