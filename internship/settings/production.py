from django.conf import settings
import os
import dj_database_url
from storages.backends.s3boto3 import S3Boto3Storage
from django.http import HttpResponseRedirect

DEBUG = False
TEMPLATE_DEBUG = False
db_from_env = dj_database_url.config(conn_max_age=5)
DATABASES = settings.DATABASES
DATABASES['default'].update(db_from_env)
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*']
# Static files (CSS, JavaScript, Images)
#  https://docs.djangoproject.com/en/1.8/howto/static-files/
#  Simplified static file serving.
#  https://warehouse.python.org/project/whitenoise/

AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_STORAGE_BUCKET_NAME = 'taanabaana'
S3DIRECT_REGION = 'ap-southeast-1'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
