from pyrogram import filters
from pyrogram.types import Message
from ishika import app
from ishika.modules.helpers.inline import start_panel

BOT_NAME = "Ishika"

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/placeholder.jpg", # <-- yaha apni image ka link daal
        caption=f"**Hey {message.from_user.mention}**\n\n"
                f"**I am {BOT_NAME}** ✨\n"
                f"**Advanced Group Manager Bot**\n\n"
                f"**Press below buttons to explore**",
        reply_markup=start_panel()
    )

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message: Message):
    await message.reply(f"**{BOT_NAME} is Online** ✅\n**I am alive and working**")
