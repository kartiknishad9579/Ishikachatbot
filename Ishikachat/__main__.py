import asyncio
from Ishikachat import app, LOGGER
from Ishikachat.modules.helpers.mongo import mongoping

async def main():
    await app.start()
    await mongoping()
    LOGGER.info(f"IshikaChatBot Started Successfully ✅")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
