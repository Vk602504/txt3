import os

API_ID    = os.environ.get("API_ID", "28328736")
API_HASH  = os.environ.get("API_HASH", "802254a44896baa87f3083b7af36b2e5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6786890612:AAEvELybEXn_j4qGnQAFdB8m9JDkgMW9uXk") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
