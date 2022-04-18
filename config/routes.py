from app.example.route import route as ExampleRoute


def register_routes(app, root: str):
  app.include_router(ExampleRoute, prefix=f'{root}/example')
