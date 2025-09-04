__PLUGIN__ = "ping"

from time import perf_counter
from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import command
from .modules import register

register("ping", "Bot latency.")

@Client.on_message(command(["ping", "alive"]))
async def ping(client: Client, message: Message):
t1 = perf_counter()
m = await message.reply_text("Pinging...")
t2 = perf_counter()
await m.edit_text(f"Pong! <b>{(t2 - t1)*1000:.0f} ms</b>")
