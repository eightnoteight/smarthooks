from aiohttp import web
from .geeksforgeeksbot import app as geeksforgeeksbot_app
from .geeksforgeeksbot import endpoint as geeksforgeeksbot_endpoint
import os

app = web.Application()
app.router.add_route('GET', geeksforgeeksbot_endpoint, geeksforgeeksbot_app)
app.router.add_route('POST', geeksforgeeksbot_endpoint, geeksforgeeksbot_app)

def main():
    web.run_app(app, port=int(os.environ.get('PORT', '5000')))
