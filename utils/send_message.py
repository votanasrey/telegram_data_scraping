import asyncio
import csv
from dotenv import load_dotenv
load_dotenv()
import os
from pyrogram import Client


# Replace these with your own API credentials from https://my.telegram.org

api_id    = os.getenv("api_id")
api_hash = os.getenv("api_hash")
my_account = os.getenv("my_account")
chat_id = os.getenv("chat_id")
user_name = os.getenv("user_name")

# Initialload_dotenv()

CONFIG = {
    "telegram_api_id": api_id,
    "telegram_hash": api_hash,
}

app = Client(my_account ,CONFIG["telegram_api_id"],CONFIG["telegram_hash"])

def send_message_to_user(user_name, message):
    with app:
        app.send_message(user_name, message)
    print("The message was sent to!", user_name)
