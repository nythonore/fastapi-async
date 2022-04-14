from modules.example.route import route as ExampleRoute


def configure_routes(app, root: str):
  app.include_router(ExampleRoute, prefix=f'{root}/example')
