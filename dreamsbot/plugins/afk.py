__PLUGIN__ = "afk"

from pyrogram import Client, filters
from pyrogram.types import Message
from dreamsbot.core.mongo import col_afk
from dreamsbot.helpers.decorators import command
from .modules import register

register("afk", "Away-from-keyboard: /afk [reason]. Mentions notify.")

@Client.on_message(command(["afk"]))
async def set_afk(client: Client, message: Message):
reason = message.text.split(None, 1)[1] if len(message.command) > 1 else "AFK"
await col_afk.update_one({"user_id": message.from_user.id}, {"$set": {"reason": reason}}, upsert=True)
await message.reply_text("You're marked AFK.")

@Client.on_message(filters.mentioned)
async def notify_afk(client: Client, message: Message):
for ent in message.entities or []:
pass
user_ids = set()
if message.entities:
for e in message.entities:
if e.user:
user_ids.add(e.user.id)
for uid in user_ids:
doc = await col_afk.find_one({"user_id": uid})
if doc:
await message.reply_text(f"User is AFK: {doc['reason']}")

@Client.on_message(filters.user)
async def clear_afk(client: Client, message: Message):
# Any message by the user clears AFK
await col_afk.delete_one({"user_id": message.from_user.id})
