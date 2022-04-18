from fastapi.exceptions import RequestValidationError, HTTPException
from config.settings import settings
from core.helpers.exception import handle_request_validation_error, handle_http_exception, handle_exception


def register_exception(app):
  app.add_exception_handler(
      RequestValidationError, handle_request_validation_error
  )

  app.add_exception_handler(HTTPException, handle_http_exception)

  if settings.APP_DEBUG is False:
    app.add_exception_handler(Exception, handle_exception)
