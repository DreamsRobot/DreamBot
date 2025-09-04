from functools import wraps
from pyrogram import filters
from dreamsbot.core.permissions import is_admin

# Require admins in group chats

def admin_only(func):
@wraps(func)
async def wrapper(client, message):
if message.chat.type in ("group", "supergroup"):
if not await is_admin(client, message.chat.id, message.from_user.id):
return await message.reply_text("You need to be an admin to use this.")
return await func(client, message)
return wrapper

# Command helper that supports multiple prefixes

def command(names, prefixes=None):
from config import Config
if prefixes is None:
prefixes = Config.COMMAND_PREFIXES
return filters.command(names, prefixes=prefixes)
