from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# kb_start
_buttons_start = [[
    KeyboardButton(text='Начать игру'),
    KeyboardButton(text='Правила игры'),
    KeyboardButton(text='Счёт'),
]]
keyboard_start = ReplyKeyboardMarkup(
    keyboard=_buttons_start,
    resize_keyboard=True
)

# kb_game
_buttons_game = [[
    KeyboardButton(text='Камень ✊🏼'),
    KeyboardButton(text='Ножницы ✌🏼'),
    KeyboardButton(text='Бумага ✋🏼')
]]
keyboard_game = ReplyKeyboardMarkup(
    keyboard=_buttons_game,
    resize_keyboard=True
)

# kb_continue
_buttons_continue = [[
    KeyboardButton(text='Сыграть ещё'),
    KeyboardButton(text='Выйти в меню')
]]
keyboard_continue = ReplyKeyboardMarkup(
    keyboard=_buttons_continue,
    resize_keyboard=True
)

# kb_score
_buttons_score = [[
    KeyboardButton(text='Сбросить счёт'),
    KeyboardButton(text='Выйти в меню')
]]
keyboard_score = ReplyKeyboardMarkup(
    keyboard=_buttons_score,
    resize_keyboard=True
)
