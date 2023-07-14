from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks.games import GamesCallbackData

guess_the_number_inline_button = InlineKeyboardButton(
    text='Угадай число',
    callback_data=GamesCallbackData(game='guess_the_number').pack()
)
rock_paper_scissors_inline_button = InlineKeyboardButton(
    text='Камень ножницы бумага',
    callback_data=GamesCallbackData(game='rps').pack()
)
magic_ball_inline_button = InlineKeyboardButton(
    text='Магический шар',
    callback_data=GamesCallbackData(game='magic_ball').pack()
)

games_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [guess_the_number_inline_button],
    [rock_paper_scissors_inline_button],
    [magic_ball_inline_button]
])