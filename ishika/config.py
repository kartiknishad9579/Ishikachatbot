import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_DB_URI = os.getenv("MONGO_DB_URI") 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

BOT_NAME = "Ishika"
BOT_USERNAME = os.getenv("BOT_USERNAME", "Ishika_Baby_bot")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/ishika_support")
