from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

hello = """
Hello, {data.from_user.first_name}!

Your id -> {data.chat.id}
Your usr -> {data.from_user.username}
"""

def kb():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [KeyboardButton(text="/start")]
        ]
    )