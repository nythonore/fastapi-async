from pydantic import BaseModel

class ErrorType(BaseModel):
  status: str = 'error'
  message: str

class FailDataType(BaseModel):
  field: str

class FailType(BaseModel):
  status: str = 'fail'
  data: FailDataType

responses = {
  400: {'model': ErrorType},
  401: {'model': ErrorType},
  403: {'model': ErrorType},
  404: {'model': ErrorType},
  422: {'model': FailType},
  500: {'model': ErrorType}
}
