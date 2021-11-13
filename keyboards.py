import telebot as t

subjects_keyboard = t.types.InlineKeyboardMarkup().add(t.types.InlineKeyboardButton(text='Физика', callback_data='Physics'),
                                                       t.types.InlineKeyboardButton(text='Математика', callback_data='Math'),
                                                       t.types.InlineKeyboardButton(text='Англиский язык', callback_data='Eng'))

lang_keyboard = t.types.InlineKeyboardMarkup().add(t.types.InlineKeyboardButton(text='Қазақша', callback_data='Kazakh'),
                                                   t.types.InlineKeyboardButton(text='Русский', callback_data='Russian'),
                                                   t.types.InlineKeyboardButton(text='English', callback_data='English'))


days_keyboard = t.types.InlineKeyboardMarkup().add(t.types.InlineKeyboardButton(text='Понедельник', callback_data='Monday'),
                                        t.types.InlineKeyboardButton(text='Вторник', callback_data='Tuesday'),
                                        t.types.InlineKeyboardButton(text='Среда', callback_data='Wednesday'),
                                        t.types.InlineKeyboardButton(text='Четверг', callback_data='Thursday'),
                                        t.types.InlineKeyboardButton(text='Пятница', callback_data='Friday'),
                                        t.types.InlineKeyboardButton(text='Суббота', callback_data='Saturday'),
                                        t.types.InlineKeyboardButton(text='Воскресенье', callback_data='Sunday'))

time_keyboard = t.types.InlineKeyboardMarkup().add(t.types.InlineKeyboardButton(text='9:00', callback_data='Nine'),
                                          t.types.InlineKeyboardButton(text='10:00', callback_data='Ten'),
                                          t.types.InlineKeyboardButton(text='11:00', callback_data='Three'),
                                          t.types.InlineKeyboardButton(text='12:00', callback_data='Four'),
                                          t.types.InlineKeyboardButton(text='13:00', callback_data='Thirteen'),
                                          t.types.InlineKeyboardButton(text='14:00', callback_data='Fourteen'),
                                          t.types.InlineKeyboardButton(text='15:00', callback_data='Fifteen'),
                                          t.types.InlineKeyboardButton(text='16:00', callback_data='Sixteen'),
                                          t.types.InlineKeyboardButton(text='17:00', callback_data='Seventeen'),
                                          t.types.InlineKeyboardButton(text='18:00', callback_data='Eighteen'),
                                          t.types.InlineKeyboardButton(text='19:00', callback_data='Nineteen'),
                                          t.types.InlineKeyboardButton(text='20:00', callback_data='Twenty'),
                                          t.types.InlineKeyboardButton(text='21:00', callback_data='Twenty one'))