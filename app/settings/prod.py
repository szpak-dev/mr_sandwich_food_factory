import dsnparse
from .defaults import *

DEBUG = False

dsn = dsnparse.parse_environ('DATABASE_DSN')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': dsn.paths[0],
        'USER': dsn.user,
        'PASSWORD': dsn.password,
        'HOST': dsn.host,
        'PORT': dsn.port,
    }
}
