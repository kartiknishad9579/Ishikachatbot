from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from ishika import app

BOT_NAME = "Ishika"

def start_panel():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ Add Me", url="https://t.me/IshikaBot?startgroup=true"),
            InlineKeyboardButton("💭 Support", url="https://t.me/Ishika_Support")
        ],
        [InlineKeyboardButton("💬 Channel", url="https://t.me/Ishika_Updates")]
    ])

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/c2d2b7beeb5d3a8b2b1a1.jpg",
        caption=f"**Hey {message.from_user.mention}**\n"
                f"**I am {BOT_NAME}** ✨\n"
                f"**Advanced Group Manager Bot**\n"
                f"**Press below buttons to explore**",
        reply_markup=start_panel()
    )

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message: Message):
    await message.reply(f"**{BOT_NAME} is Online** ✅")
