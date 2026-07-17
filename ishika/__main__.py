import asyncio
import signal
from ishika import app, LOGGER
from ishika.modules.helpers.mongo import mongoping

async def shutdown():
    """Graceful shutdown"""
    LOGGER.info("Shutting down IshikaBot...")
    await app.stop()
    await app.shutdown()

async def main():
    # 1. Mongo Connect
    LOGGER.info("Connecting to MongoDB...")
    await mongoping()
    
    # 2. Bot Start
    await app.start()
    me = await app.get_me()
    LOGGER.info(f"Bot logged in as @{me.username} ✅")
    LOGGER.info("IshikaChatBot Started Successfully ✅")
    
    # 3. Run Bot
    await app.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        LOGGER.info("Bot stopped by user")
    except Exception as e:
        LOGGER.error(f"Fatal error: {e}")
