from tortoise.contrib.fastapi import register_tortoise as config_tortoise
from config.settings import settings

DB_URL = f'postgres://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}'

TORTOISE_MODULES = ['app.example.model']


def register_tortoise(app):
  config_tortoise(
      app,
      db_url=DB_URL,
      modules={'models': TORTOISE_MODULES},
      generate_schemas=True,
      add_exception_handlers=True,
  )
