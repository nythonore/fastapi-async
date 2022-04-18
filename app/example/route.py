from fastapi import APIRouter, HTTPException, status
from app.example.schema import ExampleListResult, ExampleSingleResult, ExamplePayload

route = APIRouter(tags=['Example'])


@route.get('', response_model=ExampleListResult, status_code=status.HTTP_200_OK)
async def list_example():
  raise HTTPException(status_code=400, detail='Hello There')


@route.post(
    '', response_model=ExampleSingleResult, status_code=status.HTTP_201_CREATED
)
async def create_example(payload: ExamplePayload):
  print(payload)
