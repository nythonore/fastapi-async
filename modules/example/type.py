from typing import List
from pydantic import BaseModel
from core.base.type import BaseType
from core.base.type import ResultType


class ExampleBase(BaseModel):
  name: str


class ExampleType(ExampleBase, BaseType):
  pass


class ExamplePayload(ExampleBase):
  pass


class ExampleSingleResult(ResultType):
  data: ExampleType


class ExampleListResult(ResultType):
  data: List[ExampleType]
