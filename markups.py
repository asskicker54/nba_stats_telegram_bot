from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_back_main = KeyboardButton('Начать заново')

# ---Main menu---
search_btn = KeyboardButton('Найти игрока 🏀')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(search_btn)

# ---After Found Menu---
stat_btn = KeyboardButton('Статистика')
comp_btn = KeyboardButton('Сравнить с другим игроком')
af_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(stat_btn, comp_btn, btn_back_main)

# ---Statistics Menu---
pss_total_btn = KeyboardButton('Play-off stats total')
pss_avg_btn = KeyboardButton('Play-off stats avg')
reg_total_btn = KeyboardButton('Regular season stats total')
reg_avg_btn = KeyboardButton('Regular seasson stats avg')
go_back_btn = KeyboardButton('Назад')
stat_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(pss_total_btn, pss_avg_btn, reg_total_btn, reg_avg_btn, go_back_btn)


