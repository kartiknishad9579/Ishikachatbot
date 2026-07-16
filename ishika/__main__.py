import asyncio
from ishika import app, LOGGER
from ishika.modules.helpers.mongo import mongoping

async def main():
    LOGGER.info("Connecting to MongoDB...")
    await mongoping()
    
    await app.start()
    me = await app.get_me()
    LOGGER.info(f"Bot logged in as @{me.username} ✅")
    LOGGER.info("IshikaChatBot Started Successfully ✅")
    await app.run()

if __name__ == "__main__":
    asyncio.run(main())
