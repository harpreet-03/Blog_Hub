"""
Production settings for deployment
"""
import os
from .settings import *

# Override settings for production
DEBUG = False

# Security settings
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.railway.app',
    '.vercel.app',
    '.render.com',
    '.herokuapp.com',
    '*'  # Temporary for Railway deployment
]

# Database for production (PostgreSQL)
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Fallback to SQLite for development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise for static file serving
if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files settings for production
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

# Railway specific settings
if 'RAILWAY_ENVIRONMENT' in os.environ:
    CSRF_TRUSTED_ORIGINS = [
        'https://*.railway.app',
        'http://localhost:8000',
        'http://127.0.0.1:8000',
    ]
