import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ishika import app
from ishika.modules.helpers.mongo import mongoping
from ishika.config import LOGGER

@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    LOGGER.info(f"[Ishika] /start command received from {message.from_user.id}")
    await message.reply_photo(
        photo="https://graph.org/file/c2d2b7beeb5d3a8b2b1a1.jpg",
        caption=f"Hey {message.from_user.first_name} I Am Ishika Chatbot\n"
                f"I Am Powered By Ishika\n"
                f"Made With Love By Ishika",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("➕ Add Me", url="https://t.me/IshikaBot?startgroup=true"),
                InlineKeyboardButton("💭 Support", url="https://t.me/Ishika_Support")
            ],
            [InlineKeyboardButton("💬 Channel", url="https://t.me/Ishika_Updates")]
        ])
    )

async def main():
    await mongoping()
    await app.start()
    me = await app.get_me()
    LOGGER.info(f"[Ishika] MongoDB Connected ✅")
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info(f"[Ishika] Handler Registered ✅")
    await app.idle()

app.run()
