import asyncio
import random
from pyrogram import filters
from ishika import app, userbot
from ishika.config import OWNER_ID, LOGGER

if userbot:
    @userbot.on_message(filters.text & filters.incoming & ~filters.bot & ~filters.me)
    async def id_chatbot_reply(client, message):
        me = await client.get_me()
        if message.reply_to_message and message.reply_to_message.from_user.id == me.id:
            replies = ["Haan bolo? 💜", "Main Ishika hu", "Kya hua?"]
            await asyncio.sleep(1.5)
            await message.reply(random.choice(replies))
            LOGGER.info(f"ID Chatbot replied in {message.chat.id}")

async def restart_idchatbots():
    LOGGER.info("ID Chatbot module loaded")
