__PLUGIN__ = "blacklist"

from pyrogram import Client, filters
from pyrogram.types import Message
from dreamsbot.core.mongo import col_blacklist
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("blacklist", "Word blacklist: /addblack <word>, /rmblack <word>, auto-delete.")

@Client.on_message(filters.text & ~filters.via_bot)
async def bl_enforce(client: Client, message: Message):
words = [doc["word"] async for doc in col_blacklist.find({"chat_id": message.chat.id})]
if not words:
return
text = message.text.lower()
for w in words:
if w in text:
try:
await message.delete()
except Exception:
pass
break

@Client.on_message(command(["addblack"]))
@admin_only
async def add_black(client: Client, message: Message):
if len(message.command) < 2:
return await message.reply_text("Usage: /addblack word")
word = message.command[1].lower()
await col_blacklist.update_one({"chat_id": message.chat.id, "word": word}, {"$set": {"word": word}}, upsert=True)
await message.reply_text("Added.")

@Client.on_message(command(["rmblack"]))
@admin_only
async def rm_black(client: Client, message: Message):
if len(message.command) < 2:
return await message.reply_text("Usage: /rmblack word")
word = message.command[1].lower()
await col_blacklist.delete_one({"chat_id": message.chat.id, "word": word})
await message.reply_text("Removed.")
