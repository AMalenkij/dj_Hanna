from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = 'abc'

DEBUG = True

ALLOWED_HOSTS = []


MEDIA_URL = '/media/'

STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



