from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.inline import games_inline_keyboard

common = Router()


@common.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(text='Привет, у меня есть для тебя 3 игры, выбери в какую будешь играть))',
                         reply_markup=games_inline_keyboard)


