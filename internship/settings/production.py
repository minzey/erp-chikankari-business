from django.conf import settings
import os
import dj_database_url


DEBUG = True
TEMPLATE_DEBUG = True
try:
    db_from_env = dj_database_url.config(conn_max_age=500)

    DATABASES = settings.DATABASES
    DATABASES['default'].update(db_from_env)

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/


    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
except:
    db_from_env = dj_database_url.config(conn_max_age=500)

    DATABASES = settings.DATABASES
    DATABASES['default'].update(db_from_env)

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/


    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
