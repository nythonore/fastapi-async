from fastapi import FastAPI
from config.settings import settings
from config.logging import configure_logging
from config.middleware import configure_middleware
from config.exception import configure_exception
from config.routes import configure_routes
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

  configure_logging()
  configure_middleware(app)
  configure_exception(app)
  configure_routes(app, root=settings.ROOT_PATH)

  return app
