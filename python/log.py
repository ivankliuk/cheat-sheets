import os
from logging.config import dictConfig

PROJECT_DIR = '/tmp/'
LOG_PATH = os.path.join(PROJECT_DIR, 'output.log')
LOGGING = {
    'version': 1,
    'formatters': {
        'file_formatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'stream_formatter': {
            'format': '[%(name)s] %(message)s'
        }
    },
    'handlers': {
        'file_handler': {
            'filename': LOG_PATH,
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file_formatter'

        },
        'stream_handler': {

            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'stream_formatter'
        },
    },
    'loggers': {
        'root-logger': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'INFO',
        },
    }
}

dictConfig(LOGGING)


# Handy logging
from inspect import stack
from logging import getLogger

log = lambda s: getLogger('%s.%s' % (s.__class__.__name__, stack()[1][3],))

# Usage
log(self).info('Logging info!')
