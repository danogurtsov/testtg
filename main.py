from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
from dotenv import load_dotenv
load_dotenv()  # грузим из .env


TOKEN = os.getenv("TELEGRAM_TOKEN")

ALLOWED_USER_ID = 358720544

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Access denied.")
        return
    await update.message.reply_text("Hey hey")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Access denied.")
        return
    await update.message.reply_text("Hey hey NEW NEW 32 OLAOLA 2")

if __name__ == "__main__":
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    app.run_polling()
