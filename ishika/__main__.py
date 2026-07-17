import asyncio
from ishika import app
from ishika.modules.helpers.mongo import mongoping
from ishika.config import LOGGER

async def main():
    await mongoping()
    await app.start()
    me = await app.get_me()
    LOGGER.info(f"[Ishika] MongoDB Connected ✅")
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info(f"[Ishika] Bot Started ✅")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
