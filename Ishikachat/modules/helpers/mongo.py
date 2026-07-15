import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

_client = MongoClient(MONGO_DB_URI)
IshikaDB = _client["IshikaChatDB"]

afk = IshikaDB.afk
notes = IshikaDB.notes
filters = IshikaDB.filters
welcome = IshikaDB.welcome
couples = IshikaDB.couples

async def mongoping():
    _client.admin.command('ping')
    print("[Ishika] MongoDB Connected ✅")
