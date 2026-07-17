import asyncio
import random
from pyrogram import filters
from ishika import userbot
from ishika.config import LOGGER

if userbot:
    @userbot.on_message(filters.reply & filters.incoming & ~filters.bot & ~filters.me)
    async def id_chatbot_reply(client, message):
        me = await client.get_me()
        if message.reply_to_message.from_user.id == me.id:
            replies = ["Haan bolo? 💜", "Main Ishika hu", "Kya hua?"]
            await asyncio.sleep(2)
            await message.reply(random.choice(replies))
            LOGGER.info(f"ID Chatbot replied in {message.chat.id}")

def restart_idchatbots():
    LOGGER.info("ID Chatbot module loaded")
