import asyncio
import os
import importlib
from ishika import app
from ishika.modules.helpers.mongo import mongoping
from ishika.config import LOGGER

async def load_modules():
    path = "ishika/modules"
    for filename in os.listdir(path):
        if filename.endswith(".py") and not filename.startswith("_"):
            module_name = f"ishika.modules.{filename[:-3]}"
            try:
                importlib.import_module(module_name)
                LOGGER.info(f"[Ishika] Loaded module: {filename[:-3]}")
            except Exception as e:
                LOGGER.error(f"[Ishika] Failed to load {filename}: {e}")

async def main():
    await mongoping()
    await app.start()
    await load_modules()
    
    me = await app.get_me()
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info("[Ishika] IshikaChatBot Started Successfully ✅")
    await app.idle()

app.run()
