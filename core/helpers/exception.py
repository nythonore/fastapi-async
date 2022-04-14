from fastapi import Request, status
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException

def handle_request_validation_error(request: Request, exception: RequestValidationError):
  error = exception.errors()[0]
  return JSONResponse(content={'error': 'fail', 'data': {f'{error["loc"][1]}': error["msg"]}}, status_code=422)

def handle_http_exception(request: Request, exception: HTTPException):
  return JSONResponse(content={'status': 'error', 'message': exception.detail}, status_code=exception.status_code)

def handle_exception(request: Request, exception: Exception):
  return JSONResponse(content={'status': 'error', 'message': 'Internal Server Error'}, status_code=500)
