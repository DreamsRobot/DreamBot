import time
from collections import defaultdict

# Simple in-memory rate limiter per (chat, user)
WINDOW = 3
MAX_CALLS = 5

_calls = defaultdict(list)

def allow(chat_id: int, user_id: int) -> bool:
now = time.time()
key = (chat_id, user_id)
_calls[key] = [t for t in _calls[key] if now - t < WINDOW]
if len(_calls[key]) >= MAX_CALLS:
return False
_calls[key].append(now)
return True
