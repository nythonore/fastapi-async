from config.app import create_app

app = create_app()

@app.on_event('startup')
async def on_startup():
  pass
