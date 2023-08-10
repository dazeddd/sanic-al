from sanic import Sanic
from sanic.response import text
import asyncio
import time

app = Sanic("MySanicApp")

# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world.")

@app.get("/sync")
def sync_handler(request):
    time.sleep(0.1)
    return text("Done")

@app.get("/async")
async def async_handler(request):
    await asyncio.sleep(0.1)
    return text("Done")
