import os, dotenv
from pydantic import BaseModel

dotenv.load_dotenv()


class BaseConfig(BaseModel):
  BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
  ROOT_PATH: str = '/v1'

  APP_NAME: str = 'FastAPI'
  APP_VERSION: str = '0.0.1'
  APP_SECRET: str = 'secret'
  APP_DEBUG: bool = True

  DB_HOST: str = 'localhost'
  DB_PORT: str = '5432'
  DB_DATABASE: str = 'fastapi'
  DB_USERNAME: str = 'postgres'
  DB_PASSWORD: str = 'password'


settings = BaseConfig(**os.environ)
