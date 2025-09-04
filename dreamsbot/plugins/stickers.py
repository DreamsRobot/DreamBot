__PLUGIN__ = "stickers"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import command
from .modules import register

register("stickers", "Sticker info: reply /sticker to a sticker.")

@Client.on_message(command(["sticker"]))
async def sticker_info(client: Client, message: Message):
if not message.reply_to_message or not message.reply_to_message.sticker:
return await message.reply_text("Reply to a sticker.")
s = message.reply_to_message.sticker
await message.reply_text(
f"Emoji: {s.emoji}\nSet: {s.set_name}\nID: <code>{s.file_unique_id}</code>\nAnimated: {s.is_animated}"
)
