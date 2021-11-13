import telebot as t
import logging
from db import DB
import keyboards as kb

bot_TOKEN = '2021796476:AAHFBze12f2JJs_NcCYF3A68n_OQPXeK3Mo'
CHANNEL_NAME = '@testchannelchanel'

bot = t.TeleBot(bot_TOKEN)


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
languages = ['English', 'Russian', 'Kazakh']
subjects = ['Math', 'Physics', 'Eng']
times = ['Nine', 'Ten', 'Eleven','Twelve', 'Thirteen','Fourteen','Fifteen', 'Sixteen','Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'Twenty one']

@bot.message_handler(commands=['start'])
def send(message):
    # connect = DB()
    # connect.conn('SELECT* ')
    # bot.send_message(CHANNEL_NAME, text='Hello')
    bot.send_message(message.from_user.id, text='Jiber your qupiyasoz, example "Alisher Qwer$yTerenoi2021"')

@bot.message_handler(commands=['create'])
def create_request(message):
    bot.send_message(message.from_user.id, text='Qai sabaq?', reply_markup=kb.subjects_keyboard)

@bot.callback_query_handler(lambda c: subjects[0] in c.data)
def math_send(c):
    bot.send_message(c.from_user.id, text=f'You chosen {subjects[0]}!', reply_markup=kb.lang_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: subjects[1] in c.data)
def phys_send(c):
    bot.send_message(c.from_user.id, text=f'You chosen {subjects[1]}!', reply_markup=kb.lang_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: subjects[2] in c.data)
def eng_send(c):
    bot.send_message(c.from_user.id, text=f'You chosen {subjects[2]}!', reply_markup=kb.lang_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)


@bot.callback_query_handler(lambda c: languages[0] in c.data)
def lang_eng(c):
    bot.send_message(c.from_user.id, text=f'{c.data} language', reply_markup=kb.days_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: languages[1] in c.data)
def lang_rus(c):
    bot.send_message(c.from_user.id, text=f'{c.data} language', reply_markup=kb.days_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: languages[2] in c.data)
def lang_kaz(c):
    bot.send_message(c.from_user.id, text=f'{c.data} language', reply_markup=kb.days_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)


@bot.callback_query_handler(lambda c: days[0] in c.data)
def days_send0(c):
    bot.send_message(c.from_user.id, text=f'{days[0]} day', reply_markup=kb.time_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: days[1] in c.data)
def days_send1(c):
    bot.send_message(c.from_user.id, text=f'{days[1]} day', reply_markup=kb.time_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: days[2] in c.data)
def days_send2(c):
    bot.send_message(c.from_user.id, text=f'{days[2]} day', reply_markup=kb.time_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: days[3] in c.data)
def days_send3(c):
    bot.send_message(c.from_user.id, text=f'{days[3]} day', reply_markup=kb.time_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: days[4] in c.data)
def days_send4(c):
    bot.send_message(c.from_user.id, text=f'{days[4]} day', reply_markup=kb.time_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: days[5] in c.data)
def days_send5(c):
    bot.send_message(c.from_user.id, text=f'{days[5]} day', reply_markup=kb.time_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: days[6] in c.data)
def days_send6(c):
    bot.send_message(c.from_user.id, text=f'{days[6]} day', reply_markup=kb.time_keyboard)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)


@bot.callback_query_handler(lambda c: times[0] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[0]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[1] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[1]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[2] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[2]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[3] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[3]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[4] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[4]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[5] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[5]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[6] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[6]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[7] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[7]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[8] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[8]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[9] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[9]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[10] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[10]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.callback_query_handler(lambda c: times[11] in c.data)
def time_send(c):
    bot.send_message(c.from_user.id, text=f'{times[11]} time')
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id)

@bot.message_handler(content_types=['text'])
def check_login(message):
    s = message.text
    if s.find(' ') > 0:
        s = s.split()
        if s[1] == 'AdAstra$Terenoi2021':
            connect = DB()
            connect.conn.execute(f'INSERT INTO SuperUsers(nickname, user_id) VALUES(?, ?);',
                                 (s[0], str(message.from_user.id)))
            connect.conn.commit()
            connect.conn.close()
            bot.send_message(message.from_user.id, text=f'Siz tirkeldiniz, {s[0]}!')
    else:
        bot.send_message(message.from_user.id, text='Sizge ruqsat joq')



# bot.delete_message(CHANNEL_NAME, 184)
#
# print(bot.get_chat(CHANNEL_NAME))

bot.infinity_polling()
