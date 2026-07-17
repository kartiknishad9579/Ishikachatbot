from pyrogram import filters
from pyrogram.types import Message
from ishika import app

@app.on_message(filters.command("ai") & filters.private)
async def ai_command(_, message: Message):
    await message.reply("AI abhi band hai. Jaldi chalu karunga 💜")
