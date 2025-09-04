import logging
import sys
from config import Config

logging.basicConfig(
level=logging.INFO,
format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
handlers=[logging.StreamHandler(sys.stdout)],
)

log = logging.getLogger("DreamBot")

async def log_to_chat(app, text: str):
if Config.LOG_CHAT_ID:
try:
await app.send_message(Config.LOG_CHAT_ID, text)
except Exception:
log.exception("Failed to send log to chat")
