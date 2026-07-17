from datetime import datetime
import random
from pyrogram import filters
from pyrogram.types import Message
from ishika import app
from ishika.modules.helpers.mongo import couples

BOT_NAME = "Ishika"

@app.on_message(filters.command("couple") & filters.group)
async def couple(client, message: Message):
    chat_id = message.chat.id
    today = datetime.now().strftime("%Y-%m-%d")

    # Check if already selected today
    data = await couples.find_one({"chat_id": chat_id, "date": today})
    if data:
        c1_u = await client.get_users(data["c1"])
        c2_u = await client.get_users(data["c2"])
        return await message.reply(
            f"**{BOT_NAME} - Today's Couple** 💑\n\n"
            f"{c1_u.mention} + {c2_u.mention} = ❤️\n\n"
            f"**Kal naya couple banega** 😉"
        )

    # Get members
    members = [m.user.id async for m in client.get_chat_members(chat_id) if not m.user.is_bot and not m.user.deleted]
    if len(members) < 2: 
        return await message.reply("**Need 2+ members**")

    c1, c2 = random.sample(members, 2)
    c1_u = await client.get_users(c1)
    c2_u = await client.get_users(c2)

    # Save to DB
    await couples.update_one(
        {"chat_id": chat_id},
        {"$set": {"chat_id": chat_id, "date": today, "c1": c1, "c2": c2}},
        upsert=True
    )

    await message.reply(
        f"**{BOT_NAME} - Today's Couple** 💑\n\n"
        f"{c1_u.mention} + {c2_u.mention} = ❤️\n\n"
        f"**Kal naya couple banega** 😉"
    )
