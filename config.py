from aiogram import types


BOT_TOKEN = 'API_TOKEN'
GROUP_ID = 'GROUP_ID'

user_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Оставить заявку")],
                                                    [types.KeyboardButton(text="Оставить отзыв")]],
                                                    resize_keyboard=True)

admin_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='Ответить', callback_data='answer')],
                                                    [types.InlineKeyboardButton(text='Отклонить', callback_data='cancel')]],
                                                    resize_keyboard=True)

# admin_keyboard = types.InlineKeyboardMarkup(row_width=2)
# admin_keyboard.insert(types.InlineKeyboardButton('Ответить', callback_data='answer'))
# admin_keyboard.insert(types.InlineKeyboardButton('Отклонить', callback_data='cancel'))
