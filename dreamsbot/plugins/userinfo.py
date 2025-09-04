__PLUGIN__ = "userinfo"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import command
from .modules import register

register("userinfo", "Get user info: /userinfo (reply or self)")

@Client.on_message(command(["userinfo"]))
async def userinfo(client: Client, message: Message):
u = message.reply_to_message.from_user if message.reply_to_message else message.from_user
text = (
f"<b>User Info</b>\n"
f"ID: <code>{u.id}</code>\n"
f"Name: {u.first_name} {u.last_name or ''}\n"
f"Username: @{u.username if u.username else 'N/A'}\n"
f"Is bot: {u.is_bot}"
)
await message.reply_text(text)
