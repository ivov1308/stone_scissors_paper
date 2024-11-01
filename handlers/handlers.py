from random import choice

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon import LEXICON_RU
from keyboards import *
from database import get_score
from services import get_result

router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    get_score(message)
    await message.answer(
        text=LEXICON_RU['start_txt'],
        reply_markup=keyboard_start
    )


@router.message(F.text == LEXICON_RU['help_btn'])
async def process_help(message: Message):
    await message.answer(
        text=LEXICON_RU['help_txt'],
        reply_markup=keyboard_start
    )


@router.message(F.text == LEXICON_RU['menu_btn'])
async def process_menu(message: Message):
    await message.answer(
        text=LEXICON_RU['menu_txt'],
        reply_markup=keyboard_start
    )


@router.message(F.text.in_([LEXICON_RU['start_game'],
                           LEXICON_RU['cont_game']]))
async def process_game(message: Message):
    await message.answer(
        text=LEXICON_RU['game'],
        reply_markup=keyboard_game
    )


@router.message(F.text == LEXICON_RU['score_btn'])
async def process_score(message: Message):
    await message.answer(
        text=get_score(message),
        reply_markup=keyboard_score
    )


@router.message(F.text == LEXICON_RU['reset_btn'])
async def process_reset(message: Message):
    await message.answer(
        text=get_score(message, reset=True)
    )


@router.message(F.text.in_([LEXICON_RU['stone'],
                           LEXICON_RU['scissors'],
                           LEXICON_RU['paper']]))
async def process_choice(message: Message):
    bot_choice = choice(['stone', 'scissors', 'paper'])
    await message.answer(LEXICON_RU[bot_choice])
    result: str = get_result(message.text, bot_choice)
    get_score(message, result=result)
    await message.answer(
        text=LEXICON_RU[result],
        reply_markup=keyboard_continue
    )


@router.message()
async def process_other(message: Message):
    await message.answer(
        text=LEXICON_RU['err']
    )
