import os

from dotenv import load_dotenv

load_dotenv()

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import requests

import re

my_id = os.getenv('MY_ID')

url = 'https://api.telegram.org/bot{}/'.format(os.getenv('BOT_API_KEY'))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    update.message.reply_text('Hi beibi <3, let here your message for me ;)')


def reply(update, context):
    method = url + 'sendMessage'

    text = update.message.text

    response = requests.get(url=method, params={
        'chat_id': my_id,
        'text': text,
    })

    print(response.url)


def main():
    updater = Updater(token='1961037910:AAGXdqZP4Dop8-Nzp5oXigXWMuIYyjkV53M')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('replyme', reply))

    dispatcher.add_handler(MessageHandler(Filters.text, reply))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
