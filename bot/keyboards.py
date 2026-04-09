from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🐱 Cat", callback_data="cat"),
            InlineKeyboardButton("⛔ Stop", callback_data="stop"),
        ]
    ])
