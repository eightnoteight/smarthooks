from telegram import Bot, Message, Chat
from telegram.ext import Dispatcher, MessageHandler, Filters
from .database import insert as insert_into_db
from .constants import TOKEN

bot = Bot(TOKEN)


def record_chat_id(message: Message):
    if message.new_chat_member is None:
        return
    # if the status is not regarding ourself, then ignore
    if message.new_chat_member.username != bot.username:
        return
    # must be a channel, can't be a group or supergroup or private
    if message.chat.type != Chat.CHANNEL:
        return
    insert_into_db(channel_id=message.chat.id)


def get_dispatcher():
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(MessageHandler([Filters.status_update], record_chat_id))
    return dispatcher
