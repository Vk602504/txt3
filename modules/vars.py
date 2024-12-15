import os

API_ID    = os.environ.get("API_ID", "20838202")
API_HASH  = os.environ.get("API_HASH", "fde3e78e3256ae13e868b39088c83838")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7816178665:AAFif8TNdDhH7cro5bVGgAFdkb25kjLIPL0") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
