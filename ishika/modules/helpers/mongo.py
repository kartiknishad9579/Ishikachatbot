from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from ishika.config import MONGO_DB_URI, LOGGER

_client = AsyncIOMotorClient(MONGO_DB_URI, serverSelectionTimeoutMS=5000)
IshikaDB = _client["IshikaDB"]

afk = IshikaDB.afk
notes = IshikaDB.notes
filters = IshikaDB.filters
welcome = IshikaDB.welcome
couples = IshikaDB.couples

async def mongoping():
    try:
        await _client.admin.command("ping")
        LOGGER.info("[Ishika] MongoDB Connected ✅")
    except ServerSelectionTimeoutError as e:
        LOGGER.error(f"[Ishika] MongoDB Connection Failed ❌ -> {e}")
        raise
