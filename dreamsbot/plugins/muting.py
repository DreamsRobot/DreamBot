__PLUGIN__ = "muting"

from datetime import timedelta
from pyrogram import Client
from pyrogram.types import Message, ChatPermissions
from dreamsbot.helpers.decorators import admin_only, command
from .modules import register

register("mute", "Mute/unmute: /mute [minutes], /unmute (reply)")

@Client.on_message(command(["mute"]))
@admin_only
async def mute_cmd(client: Client, message: Message):
if not message.reply_to_message:
return await message.reply_text("Reply to user to mute.")
until_date = None
if len(message.command) > 1 and message.command[1].isdigit():
until_date = message.date + timedelta(minutes=int(message.command[1]))
try:
await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
await message.reply_text("Muted.")
except Exception as e:
await message.reply_text(f"Failed: <code>{e}</code>")

@Client.on_message(command(["unmute"]))
@admin_only
async def unmute_cmd(client: Client, message: Message):
try:
await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, permissions=message.chat.permissions)
await message.reply_text("Unmuted.")
except Exception as e:
await message.reply_text(f"Failed: <code>{e}</code>")
