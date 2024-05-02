import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router
import config


async def main():
   bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
   dp = Dispatcher(storage=MemoryStorage())
   dp.include_router(router)
   await bot.delete_webhook(drop_pending_updates=True)
   await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
   
   
   @dp.callback_query_handler(lambda c: c.data == 'answer')
   async def handle_answer_button(callback_query: types.CallbackQuery):
      print(callback_query)
      await callback_query.answer('Вы ответили на вопрос')

   @dp.callback_query_handler(lambda c: c.data == 'cancel')
   async def handle_cancel_button(callback_query: types.CallbackQuery):
      print(callback_query)
      await callback_query.answer('Вопрос был отклонён техподдержкой')


if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO)
   asyncio.run(main())