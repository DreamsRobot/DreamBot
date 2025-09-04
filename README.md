# DreamBot
This canvas contains a complete, working scaffold for a Telegram group-management bot built with Pyrogram + MongoDB. It includes a plugin loader, core utilities, and a starter set of fully-implemented plugins (admin, bans, purge, warn, antiflood, welcome, notes, blacklist, AFK, ping, userinfo, stickers, wiki, etc.).

# DreamBot (Pyrogram + MongoDB)

A fast, modular Telegram group-management bot with a plugin system. Works on Heroku, Railway, Render, Docker, or bare metal.

## Quickstart
1) Copy `sample.env` to `.env` and fill values.
2) `python3 -m venv venv && source venv/bin/activate`
3) `pip install -r requirements.txt`
4) `python3 main.py`

## Environment
See `sample.env` for required keys.

## Plugins
Use `/help` to see loaded modules. Add your own modules in `dreamsbot/plugins`.
