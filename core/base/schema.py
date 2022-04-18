from datetime import datetime
from pydantic import BaseModel


class BaseType(BaseModel):
  id: int
  created_at: datetime
  updated_at: datetime


class ResultType(BaseModel):
  status: str = 'success'

  class Config:
    orm_mode = True
