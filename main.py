import asyncio
import csv
from dotenv import load_dotenv
load_dotenv()
import os
from pyrogram import Client
from utils.get_history import get_chat_history_from_user
from utils.send_message import send_message_to_user

api_id    = os.getenv("api_id")
api_hash = os.getenv("api_hash")
phone_number = os.getenv("phone_number")
my_account = os.getenv("my_account")
chat_id = os.getenv("chat_id")
user_name = os.getenv("user_name")

CONFIG = {
    "telegram_api_id": api_id,
    "telegram_hash": api_hash,
}
app = Client(my_account ,CONFIG["telegram_api_id"],CONFIG["telegram_hash"])

#========================= Action ========================= 

app.run(get_chat_history_from_user(user_name))
app.run(send_message_to_user(user_name, "Hi, This is a bot, Nice to know you!"))