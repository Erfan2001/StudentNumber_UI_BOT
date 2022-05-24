import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import json
import requests
import time
import random
PORT = int(os.environ.get('PORT', 5000))
TOKEN="5250332555:AAFXN5rrYAYJrS-sP3EYPS108sMbk5XiW-c"
# Configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    users: list = []
    with open('x.json', encoding="utf8") as f:
        users = json.load(f).get("users")
    savedData: dict = {}
    for key, value in update.message.chat.to_dict().items():
        savedData[key.strip()] = str(value).strip()
    users.append(savedData)
    res: list = []
    [res.append(x) for x in users if x not in res]
    res = {"users": res}
    with open('x.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=4))
    update.message.reply_text("""
    سلام
    عرفان نوربخش هستم:)
    شماره دانشجویی های تمام دانشجویان دانشگاه اصفهان
    """)


def studentNumber(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    user = update.message.from_user
    update.message.reply_text(user)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("برای استفاده از بات /start را وارد کنید :)")


def main() -> None:
    """Run the bot."""
    # updater = Updater("5250332555:AAFXN5rrYAYJrS-sP3EYPS108sMbk5XiW-c")
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(
        CommandHandler('studentNumber', studentNumber))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    # Start the Bot
    updater.start_polling()


if __name__ == '__main__':
    main()
