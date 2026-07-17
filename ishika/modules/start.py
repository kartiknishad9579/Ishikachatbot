from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from ishika import app
from ishika.config import LOGGER

BOT_NAME = "Ishika"

def start_panel():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ Add Me", url="https://t.me/Ishika_Baby_bot?startgroup=true"),
            InlineKeyboardButton("💭 Support", url="https://t.me/ishika_chat")
            InlineKeyboardButton("❤️ OWNER", url="https://t.me/KARTIK_NISHAD_3")
        ],
        [InlineKeyboardButton("💬 Channel", url="https://t.me/ye_duniya_ek_sapna_he")]
    ])

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    LOGGER.info(f"[Ishika] /start hit by {message.from_user.id}")
    await message.reply_photo(
        photo="https://i.ibb.co/Nd4GDnt6/IMG-20260714-WA5521.jpg", # ✅ Naya link daal diya
        caption=f"**Hey {message.from_user.mention}**\n"
                f"**I am {BOT_NAME}** ✨\n"
                f"**Advanced Group Manager Bot**\n"
                f"**Press below buttons to explore**",
        reply_markup=start_panel()
    )

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message: Message):
    await message.reply(f"**{BOT_NAME} is Online** ✅")
