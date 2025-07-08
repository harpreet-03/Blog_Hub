import os
import sys

# Add the django_web_app directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'django_web_app'))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web_app.settings')

# Import Django WSGI application
try:
    from django_web_app.wsgi import application
except ImportError:
    # Fallback import path
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

# Vercel expects the WSGI application to be named 'app'
app = application
