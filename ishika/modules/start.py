from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from ishika import app
from ishika.config import LOGGER, OWNER_ID # OWNER_ID import kar liya

BOT_NAME = "Ishika"

def start_panel():
    buttons = [
        [
            InlineKeyboardButton("➕ Add Me", url="https://t.me/Ishika_Baby_bot?startgroup=true"),
            InlineKeyboardButton("💭 Support", url="https://t.me/ishika_chat") # <-- Yaha comma add kiya
        ],
        [InlineKeyboardButton("💬 Channel", url="https://t.me/ye_duniya_ek_sapna_he")]
    ]
    
    # OWNER button sirf owner ko dikhega
    if message.from_user.id == OWNER_ID: # ye baad me add karenge
        buttons[0].append(InlineKeyboardButton("❤️ OWNER", url="https://t.me/KARTIK_NISHAD_3"))
    
    return InlineKeyboardMarkup(buttons)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    LOGGER.info(f"[Ishika] /start hit by {message.from_user.id}")
    
    buttons = [
        [
            InlineKeyboardButton("➕ Add Me", url="https://t.me/Ishika_Baby_bot?startgroup=true"),
            InlineKeyboardButton("💭 Support", url="https://t.me/ishika_chat")
        ],
        [InlineKeyboardButton("💬 Channel", url="https://t.me/ye_duniya_ek_sapna_he")]
    ]
    
    # Agar user owner hai to OWNER button add kar do
    if message.from_user.id == OWNER_ID:
        buttons[0].append(InlineKeyboardButton("❤️ OWNER", url="https://t.me/KARTIK_NISHAD_3"))
    
    await message.reply_photo(
        photo="https://i.ibb.co/Nd4GDnt6/IMG-20260714-WA5521.jpg",
        caption=f"**Hey {message.from_user.mention}**\n"
                f"**I am {BOT_NAME}** ✨\n"
                f"**Advanced Group Manager Bot**\n"
                f"**Press below buttons to explore**",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message:
