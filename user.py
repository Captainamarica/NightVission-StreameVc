"""
This Project Under Team-Silent💞 < @SILENT_DEVS >
Orgination Github Of this TeamSilent < https://github.com/TeamSilentt > Check out
Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
Found on github < https://github.com/HYPER-AD17 >
©Team Silent™
"""

from config import Config
from pyrogram import Client

REPLY_MESSAGE=Config.REPLY_MESSAGE

if REPLY_MESSAGE is not None:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH,
        plugins=dict(root="plugins.userbot")
        )
else:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH
        )
USER.start()
