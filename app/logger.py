from os import getenv

_WSGI_LOG_LEVEL = getenv('WSGI_LOG_LEVEL', 'NO_WSGI')
_APP_LOG_LEVEL = getenv('APP_LOG_LEVEL', 'WARNING')

MY_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'app': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'formatter': 'app',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': _APP_LOG_LEVEL,
    },
}
