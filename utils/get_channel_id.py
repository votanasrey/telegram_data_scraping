from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
load_dotenv()

bot_token = os.environ.get('bot_token')


def get_chat_id(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(f"Chat ID: {chat_id}")
    print(chat_id)


updater = Updater(bot_token, update_queue=None)
dp = updater.dispatcher
dp.add_handler(CommandHandler("get_chat_id", get_chat_id))

updater.start_polling()
updater.idle()