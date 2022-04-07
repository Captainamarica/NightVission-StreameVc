"""
This Project Under Team-Silent💞 < @SILENT_DEVS >
Orgination Github Of this TeamSilent < https://github.com/TeamSilentt > Check out
Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
Found on github < https://github.com/HYPER-AD17 >
©Team Silent™
"""
import asyncio
from config import Config, STREAM
from pyrogram.types import Message
from utils import mp, RADIO, USERNAME
from pyrogram import Client, filters, emoji

ADMINS=Config.ADMINS
CHAT_ID=Config.CHAT_ID
LOG_GROUP=Config.LOG_GROUP

async def is_admin(_, client, message: Message):
    admins = await mp.get_admins(CHAT_ID)
    if message.from_user is None and message.sender_chat:
        return True
    if message.from_user.id in admins:
        return True
    else:
        return False

ADMINS_FILTER = filters.create(is_admin)


@Client.on_message(filters.command(["radio", f"radio@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(CHAT_ID) | filters.private | filters.chat(LOG_GROUP)))
async def radio(_, message: Message):
    if 1 in RADIO:
        k=await message.reply_text(f"{emoji.ROBOT} `ᴘʟᴇᴀsᴇ sᴛᴏᴘ ᴇxɪsᴛɪɴɢ ʀᴀᴅɪᴏ sᴛʀᴇᴀᴍ!​`")
        await mp.delete(k)
        await message.delete()
        return
    await mp.start_radio()
    k=await message.reply_text(f"{emoji.CHECK_MARK_BUTTON} `ʀᴀᴅɪᴏ sᴛʀᴇᴀᴍ sᴛᴀʀᴛᴇᴅ​!`: \n<code>{STREAM}</code>")
    await mp.delete(k)
    await mp.delete(message)

@Client.on_message(filters.command(["stopradio", f"stopradio@{USERNAME}"]) & ADMINS_FILTER & (filters.chat(CHAT_ID) | filters.private | filters.chat(LOG_GROUP)))
async def stop(_, message: Message):
    if 0 in RADIO:
        k=await message.reply_text(f"{emoji.ROBOT} `ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ᴀ ʀᴀᴅɪᴏ sᴛʀᴇᴀᴍ ꜰɪʀsᴛ🧚‍♀️!​`")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.stop_radio()
    k=await message.reply_text(f"{emoji.CROSS_MARK_BUTTON} `ʏᴏʏᴏ ʀᴀᴅɪᴏ sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ​🚶`")
    await mp.delete(k)
    await mp.delete(message)
