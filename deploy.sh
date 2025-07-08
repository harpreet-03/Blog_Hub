#!/bin/bash

# Django File Sharing App - Deployment Script
# This script helps prepare your app for deployment

echo "🚀 Django File Sharing App - Deployment Preparation"
echo "================================================="

# Check if we're in the right directory
if [ ! -f "django_web_app/manage.py" ]; then
    echo "❌ Error: Please run this script from the Django-WebApp root directory"
    exit 1
fi

echo "📁 Current directory: $(pwd)"
echo ""

# Install production dependencies
echo "📦 Installing production dependencies..."
cd django_web_app
pip install -r requirements.txt

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser prompt
echo ""
echo "👤 Would you like to create a superuser? (y/n)"
read -r create_superuser
if [ "$create_superuser" = "y" ] || [ "$create_superuser" = "Y" ]; then
    python manage.py createsuperuser
fi

cd ..

echo ""
echo "✅ Deployment preparation complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Choose your deployment platform:"
echo "   • Railway (Recommended): railway.app"
echo "   • Render: render.com" 
echo "   • Heroku: heroku.com"
echo ""
echo "2. Set environment variables:"
echo "   • SECRET_KEY"
echo "   • DATABASE_URL (for PostgreSQL)"
echo "   • DJANGO_SETTINGS_MODULE=django_web_app.production_settings"
echo ""
echo "3. Deploy using the platform-specific method"
echo ""
echo "📚 See README.md for detailed deployment instructions"
