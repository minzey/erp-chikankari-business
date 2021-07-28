from django.conf import settings
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False
db_from_env = dj_database_url.config(conn_max_age=5)
DATABASES = settings.DATABASES
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
