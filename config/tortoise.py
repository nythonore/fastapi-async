from tortoise.contrib.fastapi import register_tortoise as config_tortoise
from config.settings import settings

DB_URL = f'postgres://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}'

TORTOISE_MODULES = ['app.example.model']

TORTOISE_ORM_MODULES = TORTOISE_MODULES
TORTOISE_ORM_MODULES.append('aerich.models')

TORTOISE_ORM = {
    'connections': {
        'default': DB_URL
    },
    'apps':
        {
            'models':
                {
                    'models': TORTOISE_ORM_MODULES,
                    'default_connection': 'default'
                }
        }
}


def register_tortoise(app):
  config_tortoise(
      app,
      db_url=DB_URL,
      modules={'models': TORTOISE_MODULES},
      generate_schemas=False,
      add_exception_handlers=True,
  )
