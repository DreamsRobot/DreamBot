__PLUGIN__ = "modules"

from pyrogram import Client
from pyrogram.types import Message
from dreamsbot.helpers.decorators import command

MODULE_DESCRIPTIONS = {}

async def init(app: Client):
# populated by other plugins on import using register()
pass

def register(module_name: str, description: str):
MODULE_DESCRIPTIONS[module_name] = description

@Client.on_message(command(["help"]))
async def help_cmd(client: Client, message: Message):
if len(message.command) == 1:
text = "<b>DreamBot Help</b>\n\n" + "\n".join(
[f"• <code>/{name}</code> — {desc}" for name, desc in sorted(MODULE_DESCRIPTIONS.items())]
)
return await message.reply_text(text)
query = message.text.split(maxsplit=1)[1].lower().strip()
for name, desc in MODULE_DESCRIPTIONS.items():
if query in (name.lower(), ):
return await message.reply_text(f"<b>{name}</b>\n{desc}")
await message.reply_text("Module not found.")
