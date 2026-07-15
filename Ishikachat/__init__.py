import asyncio
import logging
from pyrogram import Client

# Event loop fix for Python 3.11+
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - [%(name)s] - %(levelname)s - %(message)s"
)

LOGGER = logging.getLogger("IshikaChatBot")

from.config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME, BOT_USERNAME

app = Client(
    "IshikaChatBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "ishikachat.modules"}
)
