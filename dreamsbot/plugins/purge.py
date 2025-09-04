__PLUGIN__ = "purge"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("purge", "Delete messages. Use /purge <count> or reply and use /purge to delete above.")

@Client.on_message(command(["purge"]))
@admin_only
async def purge(client: Client, message: Message):
if message.reply_to_message:
start_id = message.reply_to_message.id
end_id = message.id
for msg_id in range(start_id, end_id + 1):
try:
await client.delete_messages(message.chat.id, msg_id)
except Exception:
pass
return
count = int(message.command[1]) if len(message.command) > 1 and message.command[1].isdigit() else 0
if count <= 0:
return await message.reply_text("Give a number or reply to a message.")
to_delete = [message.id]
async for m in client.search_messages(message.chat.id, from_user="me", limit=count):
to_delete.append(m.id)
try:
await client.delete_messages(message.chat.id, to_delete)
except Exception:
pass
