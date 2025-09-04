from pyrogram import filters
from config import Config

owner_filter = filters.user(Config.OWNER_ID)

admin_rights = ("can_delete_messages", "can_restrict_members", "can_promote_members")
