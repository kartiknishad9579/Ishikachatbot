import asyncio
import glob
from ishika import app
from ishika.modules.helpers.mongo import mongoping
from ishika.config import LOGGER

async def load_modules():
    path = "ishika/modules/*.py"
    files = glob.glob(path)
    for name in files:
        module_name = name.replace("ishika/modules/", "").replace(".py", "")
        __import__(f"ishika.modules.{module_name}")
        LOGGER.info(f"[Ishika] Loaded module: {module_name}")

async def main():
    await mongoping()
    await app.start()
    await load_modules()
    
    me = await app.get_me()
    LOGGER.info(f"[Ishika] Bot logged in as @{me.username} ✅")
    LOGGER.info("[Ishika] IshikaChatBot Started Successfully ✅")
    await app.idle()

app.run()
