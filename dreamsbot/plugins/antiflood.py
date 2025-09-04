__PLUGIN__ = "antiflood"

import time
from collections import defaultdict
from pyrogram import Client, filters
from pyrogram.types import Message
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("antiflood", "Limit messages per user. /setflood <count> in 5s window.")

WINDOW = 5
_counts = defaultdict(list) # (chat,user) -> timestamps
_chat_limits = defaultdict(lambda: 5)

@Client.on_message(filters.group & ~filters.service)
async def flood_guard(client: Client, message: Message):
chat, user = message.chat.id, message.from_user.id if message.from_user else 0
now = time.time()
key = (chat, user)
_counts[key] = [t for t in _counts[key] if now - t <= WINDOW]
_counts[key].append(now)
limit = _chat_limits[chat]
if len(_counts[key]) > limit:
try:
await client.restrict_chat_member(chat, user, permissions=message.chat.permissions)
await message.reply_text("Calm down. You are rate limited.")
except Exception:
pass

@Client.on_message(command(["setflood"]))
@admin_only
async def setflood(client: Client, message: Message):
if len(message.command) < 2 or not message.command[1].isdigit():
return await message.reply_text("Usage: /setflood 5")
_chat_limits[message.chat.id] = int(message.command[1])
await message.reply_text("Flood limit updated.")
