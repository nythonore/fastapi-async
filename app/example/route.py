from fastapi import APIRouter, HTTPException, status
from app.example.model import Example
from app.example.schema import ExampleListResult, ExampleSingleResult, ExamplePayload

route = APIRouter(tags=['Example'])


@route.get('', response_model=ExampleListResult, status_code=status.HTTP_200_OK)
async def list_example():
  query = await Example.all()
  return ExampleListResult(data=query)


@route.post(
    '', response_model=ExampleSingleResult, status_code=status.HTTP_201_CREATED
)
async def create_example(payload: ExamplePayload):
  query = await Example.create(**payload.dict())
  return ExampleSingleResult(data=query)
