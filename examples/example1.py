# -*- coding: utf-8 -*-
from tgclientpro import *

token = "your token"

bot = TelegramBot(token)


@bot.command(r'^/(start)$')
def start(message, args):

    bot.sendMessage(message['chat']['id'], "Hello", reply_markup={
        'inline_keyboard': [
            [
                {'text': "Hello, World", 'callback_data': '.'},
                {'text': "Hello, World", 'callback_data': '.'},
                {'text': "Hello, World", 'callback_data': '.'}
            ],
            [
                {'text': "Hello, World", 'callback_data': '.'},
            ],
            [
                {'text': "Hello, World", 'callback_data': '.'},
                {'text': "Hello, World", 'callback_data': '.'}
            ]
        ]
    })


@bot.command(r'^/(pin)')
def pin_message(message):
    if message['reply_to_message']:
        reply = message['reply_to_message']

        if message['chat']['type'] == 'supergroup':

            bot.pinChatMessage(message['chat']['id'], reply['message_id'])



@bot.inline_query()
def inline_query(inline):

    bot.answerInlineQuery(inline['id'], results=[
        {
            'type': 'article',
            'id': '1',
            'title': "Hello, World",
            'input_message_content': {
                'message_text': "Hello, World"
            }
        }
    ])

@bot.callback_query()
def callback_query(callback_query):
    bot.answerCallbackQuery(
        callback_query['id'], 'Hello'
    )

bot.run(report_http_errors=False)
