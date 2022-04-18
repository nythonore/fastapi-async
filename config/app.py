from fastapi import FastAPI
from config.settings import settings
from config.logging import register_logging
from config.middleware import register_middleware
from config.tortoise import register_tortoise
from config.exception import register_exception
from config.routes import register_routes
from core.helpers.responses import responses


def create_app():
  app = FastAPI(
      title=settings.APP_NAME,
      description=None,
      version=settings.APP_VERSION,
      docs_url=None,
      redoc_url=f'{settings.ROOT_PATH}/docs',
      openapi_url=f'{settings.ROOT_PATH}/openapi.json',
      responses=responses,
  )

  register_logging()
  register_middleware(app)
  register_tortoise(app)
  register_exception(app)
  register_routes(app, root=settings.ROOT_PATH)

  return app
