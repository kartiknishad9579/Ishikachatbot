from pyrogram import Client
from ishika.config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "IshikaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
