from aiogram import Bot, types, F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import config


router = Router()


class Form(StatesGroup):
    feedback = State()
    request = State()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет!\nЯ бот техподдержки тату-салона Честь!\n"
                     "Отправь мне любое сообщение и я тебе обязательно отвечу!", reply_markup=config.user_keyboard)
    

@router.message(StateFilter(None), F.text == "Оставить заявку")
async def put_request(message: types.Message, bot: Bot, state: FSMContext):
    await message.reply("Напишите свой вопрос и наша специалисты оперативно ответят на него", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.request)
    

@router.message(Form.request)
async def send_request(message: types.Message, bot: Bot, state: FSMContext):
    await state.update_data(request=message.text)
    await message.reply("Отлично! Ваш вопрос передан специалистам!", reply_markup=config.user_keyboard)
    await bot.send_message(chat_id=config.GROUP_ID, 
                           text=f'Новый вопрос от пользователя @{message.chat.username}\n'
                           f'{message.text}',
                           reply_markup=config.admin_keyboard)
    await state.clear()


@router.message(StateFilter(None), F.text == "Оставить отзыв")
async def put_feedback(message: types.Message, bot: Bot, state: FSMContext):
    await message.reply("Напишите всё, что думаете о нашем боте :)", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.feedback)
    

@router.message(Form.feedback)
async def send_feedback(message: types.Message, bot: Bot, state: FSMContext):
    await state.update_data(feedback=message.text)
    await message.reply("Спасибо! Ваше мнение очень важно для нас!", reply_markup=config.user_keyboard)
    await bot.send_message(chat_id=config.GROUP_ID, 
                           text=f'Новый отзыв от пользователя @{message.chat.username}\n'
                           f'{message.text}')
    await state.clear()
    

@router.message()
async def message_handler(msg: Message, bot: Bot):
    await msg.answer(f"Твой ID: {msg.from_user.id}")