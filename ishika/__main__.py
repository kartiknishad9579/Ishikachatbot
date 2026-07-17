import asyncio
from ishika import app
from ishika.modules.helpers.mongo import mongoping
from ishika.config import LOGGER

async def main():
    await mongoping()
    await app.start()
    
    # Modules load
    import ishika.modules.start
    LOGGER.info("[Ishika] Loaded module: start ✅")
    
    me = await app.get_me()
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info("[Ishika] IshikaChatBot Started Successfully ✅")
    await app.idle()

if __name__ == "__main__":
    app.run()
