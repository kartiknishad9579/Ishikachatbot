from ishika import app
from ishika.config import LOGGER
import asyncio

# Sab handlers yaha import honge
from ishika import handlers 

if __name__ == "__main__":
    LOGGER.info("[Ishika] Starting Bot...")
    app.run()
