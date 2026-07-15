import asyncio
from ishikachat import app, LOGGER
from ishikachat.modules.helpers.mongo import mongoping

async def main():
    await app.start()
    await mongoping()
    LOGGER.info(f"IshikaChatBot Started Successfully ✅")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
