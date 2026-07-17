from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from ishika.config import MONGO_DB_URI, LOGGER

_client = AsyncIOMotorClient(MONGO_DB_URI, serverSelectionTimeoutMS=5000)
IshikaDB = _client["IshikaDB"] # <- naam same rakha jo URI me hai

afk = IshikaDB.afk
notes = IshikaDB.notes
filters = IshikaDB.filters
welcome = IshikaDB.welcome
couples = IshikaDB.couples


async def mongoping():
    try:
        await _client.admin.command("ping") # <- await lag gaya
        LOGGER.info("[Ishika] MongoDB Connected ✅")
    except ServerSelectionTimeoutError as e:
        LOGGER.error(f"[Ishika] MongoDB Connection Failed ❌ -> {e}")
        raise
