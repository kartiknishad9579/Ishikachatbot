from ishika import app
from ishika.config import LOGGER

# YE LINE CHANGE KAR
from ishika.modules import start 

if __name__ == "__main__":
    LOGGER.info("[Ishika] Starting Bot...")
    app.run()
