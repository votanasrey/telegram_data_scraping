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

chat_id = int(chat_id)
# Initialload_dotenv()

CONFIG = {
    "telegram_api_id": api_id,
    "telegram_hash": api_hash,
}


async def get_group_members_list(chat_id):
   async with Client(my_account, api_id, api_hash) as app:
        async for member in app.get_chat_members(chat_id, limit=0):
            print(member.user.phone_number)
            #print(member.user)
            
asyncio.run(get_group_members_list(chat_id))
    



