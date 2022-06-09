from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import markups as nav
from nba import find_player_by_name, get_player_stats

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

class UserState(StatesGroup):
    main_player = State()
    player2 = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, {0.first_name}!'.format(message.from_user),\
         reply_markup=nav.main_menu)

@dp.message_handler(text='Найти игрока 🏀')
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите полное имя игрока')
    await UserState.main_player.set()

@dp.message_handler(state=UserState.main_player)
async def get_player_name(message: types.Message, state: FSMContext):
        await state.update_data(main_player=message.text)
        await state.reset_state(with_data=False)
        await bot.send_message(message.from_user.id, 'Выберите раздел информации об игроке', reply_markup=nav.af_menu)

@dp.message_handler(Text(equals='Статистика'))
async def info_menu(message: types.Message): 
    await bot.send_message(message.from_user.id, 'Выберите тип статистики', reply_markup=nav.stat_menu)

@dp.message_handler(Text(equals='Сравнить с другим игроком'))
async def get_compare_player_name(message: types.Message):
    await message.reply('Введите имя игрока для сравнения')
    await UserState.player2.set()

@dp.message_handler(Text(equals='Начать заново'))
async def go_back(message: types.Message):
    await bot.send_message(message.from_user.id,'Меню', reply_markup=nav.main_menu)
    

@dp.message_handler(state=UserState.player2)
async def compare_players(message: types.Message, state: FSMContext):
    await state.update_data(player2=message.text)
    await state.reset_state(with_data=False)
    data = await state.get_data()
    p1 = get_player_stats(find_player_by_name(data['main_player']))[1]
    p2 = get_player_stats(find_player_by_name(data['player2']))[1]
    
    await bot.send_message(message.from_user.id, f"PLAY-OFFS AVG:\n"
        f"\n•PTS: {round(p1['post_season']['PTS'] - p2['post_season']['PTS'], 2)}"
        f"\n•AST: {round(p1['post_season']['AST'] - p2['post_season']['AST'], 2)}"
        f"\n•REB: {round(p1['post_season']['REB'] - p2['post_season']['REB'], 2)}"
        f"\n•BLK: {round(p1['post_season']['BLK'] - p2['post_season']['BLK'], 2)}"
        f"\n•STL: {round(p1['post_season']['STL'] - p2['post_season']['STL'], 2)}"
        f"\n•TOV: {round(p1['post_season']['TOV'] - p2['post_season']['TOV'], 2) * -1}"
        f"\n\nREGULAR SEASON AVG:\n"
        f"\n•PTS: {round(p1['reg_season']['PTS'] - p2['reg_season']['PTS'], 2)}"
        f"\n•AST: {round(p1['reg_season']['AST'] - p2['reg_season']['AST'], 2)}"
        f"\n•REB: {round(p1['reg_season']['REB'] - p2['reg_season']['REB'], 2)}"
        f"\n•BLK: {round(p1['reg_season']['BLK'] - p2['reg_season']['BLK'], 2)}"
        f"\n•STL: {round(p1['reg_season']['STL'] - p2['reg_season']['STL'], 2)}"
        f"\n•TOV: {round(p1['reg_season']['TOV'] - p2['reg_season']['TOV'], 2) * -1}"
        )
 
    
@dp.message_handler()
async def info_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    stats = get_player_stats(find_player_by_name(data['main_player']))
    total, avg = stats[0], stats[1]
    if message.text == 'Play-off stats total':
        await bot.send_message(message.from_user.id, f"PLAY-OFFS TOTAL:\n"
        f"\n•Games: {total['post_season']['G']}"
        f"\n•PTS: {total['post_season']['PTS']}"
        f"\n•AST: {total['post_season']['AST']}"
        f"\n•REB: {total['post_season']['REB']}"
        f"\n•BLK: {total['post_season']['BLK']}"
        f"\n•STL: {total['post_season']['STL']}"
        f"\n•TOV: {total['post_season']['TOV']}"
        )
        
    elif message.text == 'Play-off stats avg':
        await bot.send_message(message.from_user.id, f"PLAY-OFFS AVG:\n"
        f"\n•PTS: {avg['post_season']['PTS']}"
        f"\n•AST: {avg['post_season']['AST']}"
        f"\n•REB: {avg['post_season']['REB']}"
        f"\n•BLK: {avg['post_season']['BLK']}"
        f"\n•STL: {avg['post_season']['STL']}"
        f"\n•TOV: {avg['post_season']['TOV']}"
        )
    elif message.text == 'Regular season stats total':
        await bot.send_message(message.from_user.id, f"REGULAR SEASON TOTAL:\n"
        f"\n•Games: {total['reg_season']['G']}"
        f"\n•PTS: {total['reg_season']['PTS']}"
        f"\n•AST: {total['reg_season']['AST']}"
        f"\n•REB: {total['reg_season']['REB']}"
        f"\n•BLK: {total['reg_season']['BLK']}"
        f"\n•STL: {total['reg_season']['STL']}"
        f"\n•TOV: {total['reg_season']['TOV']}"
        )
    elif message.text == 'Regular seasson stats avg':
        await bot.send_message(message.from_user.id, f"REGULAR SEASON AVG:\n"
        f"\n•PTS: {avg['reg_season']['PTS']}"
        f"\n•AST: {avg['reg_season']['AST']}"
        f"\n•REB: {avg['reg_season']['REB']}"
        f"\n•BLK: {avg['reg_season']['BLK']}"
        f"\n•STL: {avg['reg_season']['STL']}"
        f"\n•TOV: {avg['reg_season']['TOV']}"
        )
    elif message.text == 'Назад':
        await bot.send_message(message.from_user.id, 'Выберите раздел информации об игроке', reply_markup=nav.af_menu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)