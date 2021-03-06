"""
This Project Under Team-Silentð < @SILENT_DEVS >
Orgination Github Of this TeamSilent < https://github.com/TeamSilentt > Check out
Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
Found on github < https://github.com/HYPER-AD17 >
Â©Team Silentâ¢.
"""
import os
import sys
import asyncio
import subprocess
from time import sleep
from threading import Thread
from signal import SIGINT
from pyrogram import Client, filters, idle
from config import Config
from utils import mp, USERNAME, FFMPEG_PROCESSES
from pyrogram.raw.functions.bots import SetBotCommands
from pyrogram.raw.types import BotCommand, BotCommandScopeDefault
from user import USER
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant

ADMINS=Config.ADMINS
CHAT_ID=Config.CHAT_ID
LOG_GROUP=Config.LOG_GROUP

bot = Client(
    "RadioPlayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins.bot")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()
        try:
            await USER.join_chat("SILENT_DEVS")
            await USER.join_chat("SILENT_BOTS")
            await USER.join_chat("SilentVerse")
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            print(e)
            pass

def stop_and_restart():
    bot.stop()
    os.system("git pull")
    sleep(10)
    os.execl(sys.executable, sys.executable, *sys.argv)


bot.run(main())
bot.start()
print("""â­ââââââââââââðà ¬ââââ®

âsÉªÊá´É´á´ Êá´á´Éªá´ á´Êá´Êá´Êâ¡â
âsá´á´á´á´s Â» sá´á´Êá´á´á´ ð¥â
âá´á´á´  Â» Éªá´'s ÊÊá´á´Êð®ð³â
âá´á´ÉªÉ´ @SILENT_DEVSâ

â°âââðà ¬âââââââââââââ¯""")
bot.send(
    SetBotCommands(
        scope=BotCommandScopeDefault(),
        lang_code="en",
        commands=[
            BotCommand(
                command="start",
                description="Start The Bot"
            ),
            BotCommand(
                command="help",
                description="Show Help Message"
            ),
            BotCommand(
                command="splay",
                description="Play Music From YouTube"
            ),
            BotCommand(
                command="song",
                description="Download Music As Audio"
            ),
            BotCommand(
                command="next",
                description="Skip The Current Music"
            ),
            BotCommand(
                command="pause",
                description="Pause The Current Music"
            ),
            BotCommand(
                command="resume",
                description="Resume The Paused Music"
            ),
            BotCommand(
                command="radio",
                description="Start Radio / Live Stream"
            ),
            BotCommand(
                command="current",
                description="Show Current Playing Song"
            ),
            BotCommand(
                command="playlist",
                description="Show The Current Playlist"
            ),
            BotCommand(
                command="joinvc",
                description="Join To The Voice Chat"
            ),
            BotCommand(
                command="leavevc",
                description="Leave From The Voice Chat"
            ),
            BotCommand(
                command="end",
                description="Stop Playing The Music"
            ),
            BotCommand(
                command="stopradio",
                description="Stop Radio / Live Stream"
            ),
            BotCommand(
                command="rplay",
                description="Replay From The Begining"
            ),
            BotCommand(
                command="rms",
                description="Clean Unused RAW PCM Files"
            ),
            BotCommand(
                command="pmute",
                description="Mute Userbot In Voice Chat"
            ),
            BotCommand(
                command="punmute",
                description="Unmute Userbot In Voice Chat"
            ),
            BotCommand(
                command="vol",
                description="Change The Voice Chat Volume"
            ),
            BotCommand(
                command="restart",
                description="Update & Restart Bot (Owner Only)"
            ),
            BotCommand(
                command="setvar",
                description="Set / Change Configs Var (For Heroku)"
            )
        ]
    )
)

@bot.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private | filters.chat(LOG_GROUP)))
async def restart(_, message: Message):
    k=await message.reply_text("ð **á´¡á´Éªá´ ...**")
    await asyncio.sleep(3)
    if Config.HEROKU_APP:
        await k.edit("ð **Êá´Ê, \nÊá´sá´á´Êá´ÉªÉ´É¢ Êá´Êá´á´...**")
        Config.HEROKU_APP.restart()
    else:
        await k.edit("ð **á´¡á´Éªá´ Òá´Ê á´ á´¡ÊÉªÊá´...**")
        process = FFMPEG_PROCESSES.get(CHAT_ID)
        if process:
            try:
                process.send_signal(SIGINT)
            except subprocess.TimeoutExpired:
                process.kill()
            except Exception as e:
                print(e)
                pass
            FFMPEG_PROCESSES[CHAT_ID] = ""
        Thread(
            target=stop_and_restart()
            ).start()
    try:
        await k.edit("â **Êá´sá´á´Êá´ á´á´É´á´ Êá´á´!**")
        await k.reply_to_message.delete()
    except:
        pass

idle()
print("\n\nRadio Player Bot Stopped, á´á´¡á´¡")
bot.stop()
