from pyrogram import Client
from ishika.config import API_ID, API_HASH, BOT_TOKEN
from ishika.config import LOGGER

app = Client(
    "IshikaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=32
)

from ishika import handlers 

LOGGER.info("[Ishika] Starting Bot...")
app.run()
