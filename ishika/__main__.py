import asyncio
import glob
import importlib
from pyrogram import Client
from ishika.modules.helpers.mongo import mongoping
from ishika.config import API_ID, API_HASH, BOT_TOKEN, LOGGER

app = Client(
    "IshikaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def load_modules():
    """Sabhi modules auto load karega"""
    path = "ishika/modules/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            pxt = a.read()
            if "__mod_name__" in pxt:
                module_name = name.split("\\")[-1].replace(".py", "")
                imported_module = importlib.import_module(f"ishika.modules.{module_name}")
                LOGGER.info(f"[Ishika] Loaded module: {imported_module.__mod_name__}")

async def main():
    await mongoping()
    await app.start()
    await load_modules() # <- ye line add ki
    me = await app.get_me()
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info("[Ishika] IshikaChatBot Started Successfully ✅")
    await app.idle()
    await app.stop()

app.run()
