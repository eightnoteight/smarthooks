from ..worker import app as celery_app
from .bot import get_dispatcher
from .bot import bot
from .database import getall as getchannels
from telegram import Update
import json
import time


dispatcher = get_dispatcher()


@celery_app.task
def main_task(payload):
    try:
        data = json.loads(payload.decode('utf-8'))
    except UnicodeDecodeError:
        return
    dispatcher.process_update(Update.de_json(data))


@celery_app.task
def send_updates():
    for channel in getchannels():
        bot.send_message(channel.channel_id, str(time.time()))

