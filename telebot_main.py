import telebot as t
import logging
from db import DB


BOT_TOKEN = '2021796476:AAHFBze12f2JJs_NcCYF3A68n_OQPXeK3Mo'
CHANNEL_NAME = '@testchannelchanel'

keyboard = t.types.InlineKeyboardMarkup()
button = t.types.InlineKeyboardButton(text='Физика', callback_data='physics')
keyboard.add(button)

bot = t.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send(message):
    # connect = DB()
    # connect.conn('SELECT* ')
    # bot.send_message(CHANNEL_NAME, text='Hello')
    bot.send_message(message.from_user.id, text = 'Jiber your qupiyasoz, example "Alisher Qwer$yTerenoi2021"')

@bot.message_handler(commands=['superuser'])
def check_login(message):
    s = message.text
    if s.find(' ') > 0:
        s = s.split()
        if s[1] == 'AdAstra$Terenoi2021':
            connect = DB()
            connect.conn.execute(f'INSERT INTO SuperUsers(nickname, user_id) VALUES(?, ?);', (s[0], str(message.from_user.id)))
            connect.conn.commit()
            connect.conn.close()
            bot.send_message(message.from_user.id, text = f'Siz tirkeldiniz, {s[0]}!')
    else:
        bot.send_message(message.from_user.id, text = 'Sizge ruqsat joq')

@bot.message_handler(commands=['delete'])
def delete(message):
    # bot.delete_message(CHANNEL_NAME, messages[-1])
    pass

@bot.message_handler(commands=['create'])
def create_request(message):
    bot.send_message(message.from_user.id, text = 'Qai sabaq', reply_markup=keyboard)

@bot.callback_query_handler(lambda c: 'physics' in c.data)
def phys_send(c):
    bot.send_message(c.from_user.id, text = 'You chosen physics!')

#
# bot.delete_message(CHANNEL_NAME, 184)
#
# print(bot.get_chat(CHANNEL_NAME))

bot.infinity_polling()