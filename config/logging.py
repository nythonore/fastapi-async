import logging
from config.settings import settings

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters':
        {
            'require_debug_false':
                {
                    '()': 'core.helpers.logging.RequireDebugFalse',
                },
            'require_debug_true':
                {
                    '()': 'core.helpers.logging.RequireDebugTrue',
                },
        },
    'formatters':
        {
            'main_formatter':
                {
                    'format':
                        '[%(levelname)s]:[%(name)s]: %(message)s '
                        '(%(asctime)s; %(filename)s:%(lineno)d)',
                    'datefmt': '%Y-%m-%d %H:%M:%S',
                },
        },
    'handlers':
        {
            'console':
                {
                    'level': 'DEBUG',
                    'filters': ['require_debug_true'],
                    'class': 'logging.StreamHandler',
                    'formatter': 'main_formatter',
                },
            'production_file':
                {
                    'level': 'INFO',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': f'{settings.BASE_DIR}/logs/production.log',
                    'maxBytes': 1024 * 1024 * 10,
                    'backupCount': 10,
                    'formatter': 'main_formatter',
                    'filters': ['require_debug_false'],
                },
            'debug_file':
                {
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': f'{settings.BASE_DIR}/logs/debug.log',
                    'maxBytes': 1024 * 1024 * 10,
                    'backupCount': 10,
                    'formatter': 'main_formatter',
                    'filters': ['require_debug_true'],
                },
        },
    'loggers':
        {
            '':
                {
                    'handlers': ['console', 'production_file', 'debug_file'],
                    'level': 'DEBUG'
                },
        }
}


def configure_logging():
  logging.config.dictConfig(DEFAULT_LOGGING)
