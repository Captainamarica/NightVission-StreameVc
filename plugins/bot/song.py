"""
This Project Under Team-Silent💞 < @SILENT_DEVS >
Orgination Github Of this TeamSilent < https://github.com/TeamSilentt > Check out
Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
Found on github < https://github.com/HYPER-AD17 >
©Team Silent™
"""
import os
import time
import ffmpeg
import asyncio
import yt_dlp
import requests
from config import Config
from utils import USERNAME, mp
from pyrogram.types import Message
from pyrogram import Client, filters
from youtube_search import YoutubeSearch

CHAT_ID=Config.CHAT_ID
LOG_GROUP=Config.LOG_GROUP

## Extra Fns 

# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


## Commands

@Client.on_message(filters.command(["song", f"song@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private | filters.chat(LOG_GROUP)))
async def song(_, message: Message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    k=await message.reply_text("🔎")
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "geo-bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "downloads/%(id)s.%(ext)s",
        }
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count > 0:
                await time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[ᴅᴇᴠᴜ ᴍᴜꜱɪᴄ]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            await k.edit('🤷‍♀️ ꜰᴏᴜɴᴅ ʟɪᴛᴇʀᴀʀʏ ɴᴏᴛɪɴɢ!​ \nᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ sᴏɴɢ ᴏʀ ᴜsᴇ ᴄᴏʀʀᴇᴄᴛ sᴘᴇʟʟɪɴɢ.​')
            return
    except Exception as e:
        await k.edit(
            "🎧 ᴇɴᴛᴇʀ ᴀɴ sᴏɴɢ ɴᴀᴍᴇ!​ \nᴇxᴀᴍᴘʟᴇ: `/song Believer`"
        )
        print(str(e))
        return
    await k.edit("📥 **ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ sᴏɴɢ ꜰʀᴏᴍ sɪʟᴇɴᴛ's ᴅᴇᴛᴀʙᴀsᴇ...​.**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        cap = f'💬 <code>ᴛɪᴛʟᴇ:</code> <a href="{link}">{title}</a>\n<code>👩‍💻ᴅᴜʀᴀᴛɪᴏ</code>: <code>{duration}</code>\n<code>🙋‍♀️ᴠɪᴇᴡs</code>: <code>{views}</code>\n🎧 <code>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:</code> {message.from_user.mention()} \n<code>✅ᴜᴘʟᴏᴀᴅᴇʀ</code>: <b><a href="https://t.me/DEVU_ROBOT">ᴅᴇᴠᴜ ʀᴏʙᴏᴛ🧚‍♀️</a></b>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await k.edit("📤 **ᴜᴘʟᴏᴀᴅɪɴɢ sᴏɴɢ​...**")
        await message.reply_audio(audio_file, caption=cap, parse_mode='HTML', title=title, duration=dur, performer=performer, thumb=thumb_name)
        await k.delete()
        await mp.delete(message)
    except Exception as e:
        await k.edit('🤷‍♀️ 404 ᴇʀʀᴏʀ ʜᴀᴘᴘᴇɴᴇᴅ \n\nᴇʀʀᴏʀ:- {e}')
        print(e)
        pass
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        pass
