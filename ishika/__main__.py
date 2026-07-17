import asyncio
from ishika import app
from ishika.modules.helpers.mongo import mongoping
from ishika.config import LOGGER

async def load_modules():
    """Saare modules auto load karega"""
    from ishika.modules import start
    LOGGER.info("[Ishika] Loaded module: Start")

async def main():
    await mongoping()
    await app.start()
    await load_modules()
    
    me = await app.get_me()
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info("[Ishika] IshikaChatBot Started Successfully ✅")
    
    await app.idle()
    await app.stop()

app.run()
