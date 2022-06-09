import logging
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
from nba_api.stats.static import players

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='Test1')
async def cmd_test1(message: types.Message):
    await message.reply("Test1")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)