import html

def mention_user(user):
if not user:
return "Unknown"
name = html.escape(user.first_name or "User")
return f"<a href='tg://user?id={user.id}'>{name}</a>"
