import os
from dotenv import load_dotenv

load_dotenv()

class Config:
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = int(os.getenv("OWNER_ID", 0))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "")

SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "")
LOG_CHAT_ID = int(os.getenv("LOG_CHAT_ID", 0))

MONGO_URI = os.getenv("MONGO_URI", "")

CASH_API_KEY = os.getenv("CASH_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
WIKI_LANGUAGE = os.getenv("WIKI_LANGUAGE", "en")

COMMAND_PREFIXES = ["/", "!", "."]
