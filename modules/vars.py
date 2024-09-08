import os

API_ID    = os.environ.get("API_ID", "28328736")
API_HASH  = os.environ.get("API_HASH", "802254a44896baa87f3083b7af36b2e5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6935892406:AAGznKehpW_ou5_jKrxtU_xiWhiHcBuVUKs") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
