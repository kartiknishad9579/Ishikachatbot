import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# Yaha direct Mongo URL daal diya
MONGO_DB_URI = "mongodb+srv://KartikNishad:kartikNishad@ishika.jgzfxou.mongodb.net/IshikaDB?retryWrites=true&w=majority&appName=Ishika"

BOT_NAME = "Ishika"
BOT_USERNAME = os.getenv("BOT_USERNAME", "Ishika_chat_bot")
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/ishika_support")
