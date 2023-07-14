from aiogram.filters.callback_data import CallbackData


class GamesCallbackData(CallbackData, prefix='games'):
    game: str  # 'guess_the_number', 'rps', 'magic_ball'