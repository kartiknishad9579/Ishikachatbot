import os
import sys
import asyncio
import importlib
import threading
from flask import Flask

from pyrogram import idle, Client
from pyrogram.types import BotCommand

from ishika.config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, LOGGER

# ====== BOT CLIENT ======
ishika = Client(
    name="IshikaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Userbot for ID Chatbot - STRING1 hoga to hi chalega
STRING1 = os.getenv("STRING1")
userbot = None
if STRING1:
    userbot = Client(
        name="IshikaUserbot",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING1
    )

# ====== MODULES LIST ======
# Yaha apne sab plugins ke naam daal de. Path: ishika/modules/
ALL_MODULES = [
    "start",
    "help", 
    "ping",
    "ai",
    "owner",
    "clone",
    "id_chatbot"
]

# ====== BOOT FUNCTION ======
async def ishika_boot():
    try:
        await ishika.start()
        bot_username = ishika.me.username
        bot_mention = ishika.me.mention
        
        LOGGER.info(f"@{bot_username} Bot Started ✅")
        
        try:
            await ishika.send_message(int(OWNER_ID), f"**{bot_mention} is Started ❤️**")
        except Exception:
            LOGGER.warning(f"OWNER_ID pe msg nahi gaya. Bot ko /start karo")
    
        # Clone aur ID Chatbot restart
        try:
            from ishika.modules.Clone import restart_bots
            from ishika.modules.Id_chatbot import restart_idchatbots
            asyncio.create_task(restart_bots())
            asyncio.create_task(restart_idchatbots())
        except Exception as e:
            LOGGER.warning(f"Clone modules nahi mile: {e}")

        # Userbot start
        if userbot:
            try:
                await userbot.start()
                await ishika.send_message(int(OWNER_ID), f"**ID-Chatbot also Started 💕**")
                LOGGER.info("Userbot Started")
            except Exception as ex:
                LOGGER.error(f"Error in starting id-chatbot :- {ex}")
                
    except Exception as ex:
        LOGGER.error(f"Error in bot start: {ex}")
        sys.exit(1)

    # Load all modules
    for module in ALL_MODULES:
        try:
            importlib.import_module(f"ishika.modules.{module}")
            LOGGER.info(f"Successfully imported : {module}")
        except Exception as e:
            LOGGER.error(f"Failed to import {module}: {e}")

    # Set Bot Commands
    try:
        await ishika.set_bot_commands(
            commands=[
                BotCommand("start", "✧ Start the bot ✧"),
                BotCommand("help", "✧ Get the help menu ✧"),
                BotCommand("ping", "✧ Check if bot is alive ✧"),
                BotCommand("ai", "✧ Talk with AI ✧"),
                BotCommand("owner", "✧ Owner Panel ✧"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")
    
    await idle()

# ====== FLASK FOR RAILWAY ======
app = Flask(__name__)
@app.route('/')
def home():
    return "Ishika Bot is running"

def run_flask():
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

# ====== MAIN ======
if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    asyncio.run(ishika_boot())
    LOGGER.info("Stopping Ishika Bot...")
