import os, dotenv
from pydantic import BaseModel

dotenv.load_dotenv()


print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class BaseConfig(BaseModel):
  BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
  ROOT_PATH: str = '/v1'

  APP_NAME: str = 'FastAPI'
  APP_VERSION: str = '0.0.1'
  APP_SECRET: str = 'secret'
  APP_DEBUG: bool = True


settings = BaseConfig(**os.environ)
