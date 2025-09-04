__PLUGIN__ = "filters"

from pyrogram import Client, filters as pyf
from pyrogram.types import Message
from dreamsbot.core.mongo import db
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("filters", "Auto-replies: /filter name text, /stop name")

col = db["filters"]

@Client.on_message(command(["filter"]))
@admin_only
async def add_filter(client: Client, message: Message):
if len(message.command) < 3:
return await message.reply_text("Usage: /filter name text")
name = message.command[1].lower()
text = message.text.split(None, 2)[2]
await col.update_one({"chat_id": message.chat.id, "name": name}, {"$set": {"text": text}}, upsert=True)
await message.reply_text("Filter added.")

@Client.on_message(command(["stop"]))
@admin_only
async def stop_filter(client: Client, message: Message):
if len(message.command) < 2:
return await message.reply_text("Usage: /stop name")
name = message.command[1].lower()
await col.delete_one({"chat_id": message.chat.id, "name": name})
await message.reply_text("Filter removed.")

@Client.on_message(pyf.text & ~pyf.via_bot)
async def run_filters(client: Client, message: Message):
cur = col.find({"chat_id": message.chat.id})
async for doc in cur:
if doc["name"] in message.text.lower():
await message.reply_text(doc["text"])
break
