import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

REPLY_MESSAGE = """خليتلك رد بالبوت ❤️

إذا رايد شي ضروري، كرر رسالتك، البوت يحولك واتساب.

يروحي، تشرفت بيكم جميعاً، لاتنسوني بدعائكم.
مع السلامة ❤️"""

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(REPLY_MESSAGE)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is missing")

    app = Application.builder().token(token).build()
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
    )
    app.run_polling()

if __name__ == "__main__":
    main()
