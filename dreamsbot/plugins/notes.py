__PLUGIN__ = "notes"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.core.mongo import col_notes
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("notes", "Save & fetch notes: /save <name> <text>, /note <name>, /notes")

@Client.on_message(command(["save"]))
@admin_only
async def save_note(client: Client, message: Message):
if len(message.command) < 3:
return await message.reply_text("Usage: /save name text")
name = message.command[1].lower()
text = message.text.split(None, 2)[2]
await col_notes.update_one(
{"chat_id": message.chat.id, "name": name},
{"$set": {"text": text}},
upsert=True,
)
await message.reply_text("Saved.")

@Client.on_message(command(["note"]))
async def get_note(client: Client, message: Message):
if len(message.command) < 2:
return await message.reply_text("Usage: /note name")
name = message.command[1].lower()
doc = await col_notes.find_one({"chat_id": message.chat.id, "name": name})
if not doc:
return await message.reply_text("Not found.")
await message.reply_text(doc["text"])

@Client.on_message(command(["notes"]))
async def list_notes(client: Client, message: Message):
cur = col_notes.find({"chat_id": message.chat.id})
names = [doc["name"] async for doc in cur]
if not names:
return await message.reply_text("No notes.")
await message.reply_text("Notes: " + ", ".join(sorted(names)))
