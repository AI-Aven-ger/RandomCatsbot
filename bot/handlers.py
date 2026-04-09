from telegram import Update
from telegram.ext import ContextTypes

from .cat_api import get_cat
from .keyboards import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Нажми кнопку 👇",
        reply_markup=main_keyboard()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "cat":
        cat_url = get_cat()

        await query.message.reply_photo(
            photo=cat_url,
            reply_markup=main_keyboard()
        )

    elif query.data == "stop":
        await query.message.reply_text("Коты остановлены 💤")
