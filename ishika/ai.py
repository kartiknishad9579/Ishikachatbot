from pyrogram import filters
from pyrogram.types import Message
from ishika import app

@app.on_message(filters.text & ~filters.command)
async def ai_chat(_, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user.is_self:
        await message.reply("Haan bolo kya baat karni hai? 💜")
