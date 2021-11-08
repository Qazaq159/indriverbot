import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram_keyboards as kb


API_TOKEN = '2021796476:AAHFBze12f2JJs_NcCYF3A68n_OQPXeK3Mo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

yerke = 1366330811



@dp.message_handler(commands=['text'])
async def ggg(message: types.Message):
    await bot.send_message(yerke, 'hello!')

# button_hi = KeyboardButton('Привет!')
#
# greet_kb = ReplyKeyboardMarkup()
# greet_kb.add(button_hi)
#
# greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)
#
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Privet!", reply_markup=greet_kb1)

#inlinekeyboard
# inline_btn_1 = InlineKeyboardButton('First button!', callback_data='button1')
# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# @dp.message_handler(commands=['1'])
# async def process_command_1(message: types.Message):
#     await message.reply("First inline button", reply_markup=inline_kb1)



# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


# jasai almadym
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
#     code = callback_query.data[-1]
#     if code.isdigit() == False:
#         code = int(code)
#     if code == 2:
#         await bot.answer_callback_query(callback_query.id, text = 'Pressed second button')
#     elif code == 5:
#         await bot.answer_callback_query(
#             callback_query.id,
#             text = 'Pressed button with no 5',
#             show_alert=True
#         )
#     else:
#         await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, f'Pressed button={code}')
#
# @dp.message_handler(commands=['2'])
# async def process_command_2(message: types.Message):
#     await message.reply("Send all possible buttons", reply_markup=kb.inline_kb_full)

# @dp.message_handler(commands=['1'])
# async def process_command_1(message: types.Message):
#     await message.reply("First inline button", reply_markup=kb.inline_kb1)
#
# @dp.callback_query_handler(lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Pressed first button!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)