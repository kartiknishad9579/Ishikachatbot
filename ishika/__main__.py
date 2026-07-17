import asyncio
from pyrogram import Client
from ishika.modules.helpers.mongo import mongoping
from ishika.config import API_ID, API_HASH, BOT_TOKEN, LOGGER

app = Client(
    "IshikaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():
    await mongoping()
    await app.start()
    me = await app.get_me()
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info("[Ishika] IshikaChatBot Started Successfully ✅")
    await app.idle()
    await app.stop()

app.run()
