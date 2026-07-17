import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message
from ishika import app, userbot
from ishika.config import LOGGER

# Jin groups/chats me reply karna hai unke ID daal de yaha
CHAT_IDS = []  # Khali rakha to sab jagah reply karega

RESPONSES = [
    "Haan bolo? 💜",
    "Main Ishika hu, kya baat hai?",
    "Mujhe yaad kiya kya? 👀",
    "Batao kya karu tumhare liye"
]

@app.on_message(filters.command("idchatbot") & filters.user(OWNER_ID))
async def toggle_idbot(_, message: Message):
    if not userbot:
        return await message.reply("STRING1 set nahi hai bhai")
    await message.reply("ID Chatbot On hai ✅")

# Userbot wala handler
if userbot:
    @userbot.on_message(filters.text & filters.incoming & ~filters.bot & ~filters.me)
    async def id_chatbot_reply(client: Client, message: Message):
        if CHAT_IDS and message.chat.id not in CHAT_IDS:
            return
        
        # Sirf jab koi mention kare ya reply kare
        if message.reply_to_message and message.reply_to_message.from_user.id == (await client.get_me()).id:
            import random
            reply = random.choice(RESPONSES)
            await asyncio.sleep(2) # Thoda delay
            await message.reply(reply)
            LOGGER.info(f"Replied in {message.chat.id}")

async def restart_idchatbots():
    LOGGER.info("ID Chatbot modules loaded")
