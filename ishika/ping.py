import time
from pyrogram import filters
from pyrogram.types import Message
from ishika import app

@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    start = time.time()
    msg = await message.reply("Pinging...")
    end = time.time()
    await msg.edit(f"Pong! `{round(end-start)*1000}ms`")
