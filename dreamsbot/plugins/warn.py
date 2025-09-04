__PLUGIN__ = "warn"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.core.mongo import col_warns
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

MAX_WARN = 3

register("warn", "Warn system: /warn, /warnings, /resetwarns")

async def _get_warns(chat_id: int, user_id: int):
doc = await col_warns.find_one({"chat_id": chat_id, "user_id": user_id})
return doc["count"] if doc else 0

async def _set_warns(chat_id: int, user_id: int, count: int):
await col_warns.update_one(
{"chat_id": chat_id, "user_id": user_id},
{"$set": {"count": count}},
upsert=True,
)

@Client.on_message(command(["warn"]))
@admin_only
async def warn_cmd(client: Client, message: Message):
if not message.reply_to_message:
return await message.reply_text("Reply to user to warn.")
uid = message.reply_to_message.from_user.id
chat = message.chat.id
count = await _get_warns(chat, uid) + 1
await _set_warns(chat, uid, count)
if count >= MAX_WARN:
try:
await client.ban_chat_member(chat, uid)
except Exception:
pass
await _set_warns(chat, uid, 0)
return await message.reply_text(f"Warned {count}/{MAX_WARN}. User banned.")
await message.reply_text(f"Warned {count}/{MAX_WARN}.")

@Client.on_message(command(["warnings"]))
async def warnings_cmd(client: Client, message: Message):
uid = message.reply_to_message.from_user.id if message.reply_to_message else message.from_user.id
count = await _get_warns(message.chat.id, uid)
await message.reply_text(f"Warnings: <b>{count}</b>")

@Client.on_message(command(["resetwarns"]))
@admin_only
async def reset_warns(client: Client, message: Message):
uid = message.reply_to_message.from_user.id if message.reply_to_message else None
if not uid:
return await message.reply_text("Reply to user to reset warnings.")
await _set_warns(message.chat.id, uid, 0)
await message.reply_text("Warnings reset.")
