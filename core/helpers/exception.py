from fastapi import Request, status, exceptions
from starlette.responses import JSONResponse


def handle_request_validation_error(
    request: Request, exception: exceptions.RequestValidationError
):
  # pylint: disable=unused-argument
  error = exception.errors()[0]
  errorKey = ''

  if len(error['loc']) == 2:
    errorKey = error['loc'][1]
  if len(error['loc']) == 1 or type(error['loc'][1]) is int:
    errorKey = 'body'

  return JSONResponse(
      content={
          'error': 'fail',
          'data': {
              f'{errorKey}': error['msg']
          }
      },
      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
  )


def handle_http_exception(
    request: Request, exception: exceptions.HTTPException
):
  # pylint: disable=unused-argument
  return JSONResponse(
      content={
          'status': 'error',
          'message': exception.detail
      },
      status_code=exception.status_code
  )


def handle_exception(request: Request, exception: Exception):
  # pylint: disable=unused-argument
  return JSONResponse(
      content={
          'status': 'error',
          'message': 'Internal Server Error'
      },
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
  )
