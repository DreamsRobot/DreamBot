__PLUGIN__ = "welcome"

from pyrogram import Client, filters
from pyrogram.types import Message
from dreamsbot.core.mongo import col_settings
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("welcome", "Welcome settings: /setwelcome <text>, /welcome on|off")

@Client.on_message(filters.new_chat_members)
async def greet(client: Client, message: Message):
doc = await col_settings.find_one({"chat_id": message.chat.id})
if doc and not doc.get("welcome_enabled", True):
return
text = (doc.get("welcome_text") if doc else None) or "Welcome, {mention}!"
for u in message.new_chat_members:
mention = f"<a href='tg://user?id={u.id}'>{u.first_name}</a>"
await message.reply_text(text.replace("{mention}", mention))

@Client.on_message(command(["setwelcome"]))
@admin_only
async def setwelcome(client: Client, message: Message):
if len(message.command) < 2:
return await message.reply_text("Usage: /setwelcome Welcome, {mention}!")
text = message.text.split(None, 1)[1]
await col_settings.update_one(
{"chat_id": message.chat.id},
{"$set": {"welcome_text": text}},
upsert=True
)
await message.reply_text("Welcome text updated.")

@Client.on_message(command(["welcome"]))
@admin_only
async def toggle_welcome(client: Client, message: Message):
if len(message.command) < 2 or message.command[1].lower() not in {"on", "off"}:
return await message.reply_text("Usage: /welcome on|off")
enabled = message.command[1].lower() == "on"
await col_settings.update_one(
{"chat_id": message.chat.id},
{"$set": {"welcome_enabled": enabled}},
upsert=True
)
await message.reply_text(f"Welcome {'enabled' if enabled else 'disabled'}.")
