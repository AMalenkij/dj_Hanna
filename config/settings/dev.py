from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = 'abc'

DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'

TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "path/to/tiny_mce")
