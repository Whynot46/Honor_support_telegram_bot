from aiogram import types


BOT_TOKEN = '7042211706:AAGD8_2flZGeqOt1UgaKm_EbSwsY_0P0Skw'
GROUP_ID = '-916045550'

user_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Оставить заявку")],
                                                    [types.KeyboardButton(text="Оставить отзыв")]],
                                                    resize_keyboard=True)

admin_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='Ответить', callback_data='answer')],
                                                    [types.InlineKeyboardButton(text='Отклонить', callback_data='cancel')]],
                                                    resize_keyboard=True)

# admin_keyboard = types.InlineKeyboardMarkup(row_width=2)
# admin_keyboard.insert(types.InlineKeyboardButton('Ответить', callback_data='answer'))
# admin_keyboard.insert(types.InlineKeyboardButton('Отклонить', callback_data='cancel'))
