from pyrogram import filters
from pyrogram.types import Message
from ishika import app

@app.on_message(filters.command("help"))
async def help(_, message: Message):
    await message.reply("**Commands:**\n/start - Start\n/help - Help\n/ping - Check\n/ai - Talk with me")
