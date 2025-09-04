from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

_client = AsyncIOMotorClient(Config.MONGO_URI)
db = _client["dreambot"]

# Collections
col_settings = db["settings"]
col_warns = db["warns"]
col_notes = db["notes"]
col_afk = db["afk"]
col_blacklist = db["blacklist"]
col_flood = db["flood"]
