from pyrogram import filters
from pyrogram.types import Message
from ishika import app
from ishika.config import OWNER_ID

@app.on_message(filters.user(OWNER_ID) & filters.command("owner"))
async def owner_panel(_, message: Message):
    await message.reply("Owner Panel: Bot is running ✅")
