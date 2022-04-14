from fastapi.middleware.cors import CORSMiddleware


def configure_middleware(app):
  app.add_middleware(
      CORSMiddleware,
      allow_origins=['*'],
      allow_credentials=False,
      allow_methods=['*'],
      allow_headers=['*'],
  )
