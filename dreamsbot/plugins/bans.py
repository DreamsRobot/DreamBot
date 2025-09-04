__PLUGIN__ = "bans"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("ban", "Ban/Unban: /ban, /unban (reply or by username/id)")

@Client.on_message(command(["ban"]))
@admin_only
async def ban(client: Client, message: Message):
target = message.reply_to_message.from_user.id if message.reply_to_message else (message.command[1] if len(message.command)>1 else None)
if not target:
return await message.reply_text("Reply or pass a user id/username.")
try:
await client.ban_chat_member(message.chat.id, target)
await message.reply_text("Banned.")
except Exception as e:
await message.reply_text(f"Failed: <code>{e}</code>")

@Client.on_message(command(["unban"]))
@admin_only
async def unban(client: Client, message: Message):
target = message.reply_to_message.from_user.id if message.reply_to_message else (message.command[1] if len(message.command)>1 else None)
if not target:
return await message.reply_text("Reply or pass a user id/username.")
try:
await client.unban_chat_member(message.chat.id, target)
await message.reply_text("Unbanned.")
except Exception as e:
await message.reply_text(f"Failed: <code>{e}</code>")
