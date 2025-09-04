__PLUGIN__ = "admin"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import admin_only, command
from dreamsbot.core.permissions import is_admin
from .modules import register

register("admin", "Admin utilities: /id, /promote, /demote (owner-only stubs)")

@Client.on_message(command(["id"]))
async def get_id(client: Client, message: Message):
user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
await message.reply_text(f"Chat ID: <code>{message.chat.id}</code>\nUser ID: <code>{user.id}</code>")

@Client.on_message(command(["promote"]))
@admin_only
async def promote(client: Client, message: Message):
if not message.reply_to_message:
return await message.reply_text("Reply to a user to promote.")
try:
await client.promote_chat_member(
message.chat.id,
message.reply_to_message.from_user.id,
can_manage_chat=True, can_change_info=True, can_delete_messages=True,
can_manage_video_chats=True, can_restrict_members=True, can_promote_members=False,
can_invite_users=True, can_pin_messages=True
)
await message.reply_text("Promoted.")
except Exception as e:
await message.reply_text(f"Failed: <code>{e}</code>")

@Client.on_message(command(["demote"]))
@admin_only
async def demote(client: Client, message: Message):
if not message.reply_to_message:
return await message.reply_text("Reply to a user to demote.")
try:
await client.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
await message.reply_text("Demoted.")
except Exception as e:
await message.reply_text(f"Failed: <code>{e}</code>")
