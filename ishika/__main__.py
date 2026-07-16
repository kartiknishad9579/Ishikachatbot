import asyncio
import os
from aiohttp import web
from pyrogram import filters

from ishika import app, LOGGER
from ishika.modules.helpers.mongo import mongoping

async def health(_request):
    return web.Response(text="Ishika is alive ✅")

async def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    web_app = web.Application()
    web_app.router.add_get("/", health)
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    LOGGER.info(f"Health-check server listening on port {port}")

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply("Hey! Main Ishika hun 💜 Kya haal hai?")

async def main():
    await mongoping()
    await run_web_server()  # health server start
    await app.start()       # bot start
    LOGGER.info("IshikaChatBot Started Successfully ✅")
    await asyncio.Event().wait()  # bot ko zinda rakho

if __name__ == "__main__":
    asyncio.run(main())
