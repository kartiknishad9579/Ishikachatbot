from pyrogram import filters
from pyrogram.types import Message
from ishikachat import app

@app.on_message(filters.command("tagall") & filters.group)
async def tagall(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("**Reply to a message to tagall**")

    members = [m.user.mention async for m in client.get_chat_members(message.chat.id) if not m.user.is_bot]
    text = " ".join(members)
    await message.reply(f"**Tagging All:**\n{text}")
