__PLUGIN__ = "wiki"

import wikipedia
from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import command
from config import Config
from .modules import register

register("wiki", "Wikipedia search: /wiki <query>")

@Client.on_message(command(["wiki"]))
async def wiki_cmd(client: Client, message: Message):
if len(message.command) < 2:
return await message.reply_text("Usage: /wiki query")
query = message.text.split(None, 1)[1]
try:
wikipedia.set_lang(Config.WIKI_LANGUAGE)
page = wikipedia.page(query, auto_suggest=True, redirect=True)
summ = wikipedia.summary(query, sentences=3, auto_suggest=True, redirect=True)
await message.reply_text(f"<b>{page.title}</b>\n{summ}\n\n{page.url}")
except Exception as e:
await message.reply_text(f"No results: <code>{e}</code>")
