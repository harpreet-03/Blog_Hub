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
    '.herokuapp.com'
]

# Database for production (PostgreSQL)
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise for static file serving
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
