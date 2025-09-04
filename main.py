import asyncio
import importlib
import pkgutil
import uvloop
from pyrogram import Client, enums
from pyrogram.types import BotCommand

from config import Config
from dreamsbot.core.logger import log
from dreamsbot.core.mongo import db

uvloop.install()

BOT_NAME = "DreamBot"

app = Client(
name=BOT_NAME,
api_id=Config.API_ID,
api_hash=Config.API_HASH,
bot_token=Config.BOT_TOKEN,
parse_mode=enums.ParseMode.HTML,
plugins=None,
)

LOADED_PLUGINS = []

async def load_plugins():
import dreamsbot.plugins as pkg
for _, module_name, _ in pkgutil.iter_modules(pkg.__path__, pkg.__name__ + "."):
mod = importlib.import_module(module_name)
if hasattr(mod, "__PLUGIN__"):
LOADED_PLUGINS.append(mod.__PLUGIN__)
if hasattr(mod, "init") and asyncio.iscoroutinefunction(mod.init):
await mod.init(app)
log.info(f"Loaded {len(LOADED_PLUGINS)} plugins: {', '.join(sorted(LOADED_PLUGINS))}")

async def set_bot_commands():
base = [
("help", "Show help"),
("ping", "Check bot latency"),
("id", "Get IDs"),
("purge", "Delete messages"),
("ban", "Ban a user"),
("warn", "Warn a user"),
("notes", "Manage notes"),
]
await app.set_bot_commands([BotCommand(c, d) for c, d in base])

async def main():
await app.start()
await db.command("ping") # test Mongo
await load_plugins()
await set_bot_commands()
log.info(f"{BOT_NAME} is up. Owner: {Config.OWNER_ID}")
await app.idle()

if __name__ == "__main__":
asyncio.run(main())
