from fastapi.middleware.cors import CORSMiddleware


def register_middleware(app):
  app.add_middleware(
      CORSMiddleware,
      allow_origins=['*'],
      allow_credentials=False,
      allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
      allow_headers=['*'],
  )
