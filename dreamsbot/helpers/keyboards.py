from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

def support_kb():
btns = []
if Config.SUPPORT_CHAT:
btns.append([InlineKeyboardButton("Support", url=f"https://t.me/{Config.SUPPORT_CHAT.strip('@')}")])
if Config.UPDATE_CHANNEL:
btns.append([InlineKeyboardButton("Updates", url=f"https://t.me/{Config.UPDATE_CHANNEL.strip('@')}")])
return InlineKeyboardMarkup(btns) if btns else None
