from .base import *

SECRET_KEY = 'abc'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_ROOT = BASE_DIR / 'media'


