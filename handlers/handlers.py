from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon import LEXICON_RU
from keyboards import *
from random import choice
from database import get_user, reset_user

router = Router()

def get_result(message: Message) -> tuple:
    items = ['Камень ✊🏼', 'Ножницы ✌🏼', 'Бумага ✋🏼']
    results = ['draw', 'lose', 'win']
    user_item = message.text
    bot_item = choice(items)
    res_ind = items.index(user_item) - items.index(bot_item)
    return user_item[-2:], bot_item[-2:], results[res_ind]


@router.message(CommandStart())
async def process_command_start(message: Message):
    get_user(message)
    await message.answer(
        text=LEXICON_RU['start'],
        reply_markup=keyboard_start
    )


@router.message(F.text == 'Выйти в меню')
async def process_menu(message: Message):
    await message.answer(
        text=LEXICON_RU['menu'],
        reply_markup=keyboard_start
    )


@router.message(F.text == 'Правила игры')
async def process_help(message: Message):
    await message.answer(
        text=LEXICON_RU['help'],
        reply_markup=keyboard_start
    )


@router.message(F.text == 'Счёт')
async def process_score(message: Message):
    user = get_user(message)
    await message.answer(
        text=f'СЧЕТ\n'
             f'{user["name"]}: {user["win"]}\n'
             f'БОТ: {user["lose"]}\n'
             f'Ничья: {user["draw"]}'
    )


@router.message(F.text.in_(['Начать игру', 'Сыграть еще']))
async def process_game(message: Message):
    await message.answer(
        text=LEXICON_RU['game'],
        reply_markup=keyboard_game
    )


@router.message(F.text.in_(['Камень ✊🏼', 'Ножницы ✌🏼', 'Бумага ✋🏼']))
async def process_choice(message: Message):
    user = get_user(message)
    result = get_result(message)
    user[result[-1]] += 1
    await message.answer(
        text=f"{user['name']} -> {result[0]} - {result[1]} <- БОТ\n\n{LEXICON_RU[result[-1]]}",
        reply_markup=keyboard_continue
    )


@router.message(F.text == 'Сброс/сначала')
async def process_reset(message: Message):
    reset_user(message)
    await message.answer(
        text=LEXICON_RU['reset']
    )


@router.message()
async def process_other(message: Message):
    await message.answer(
        text=LEXICON_RU['err']
    )
