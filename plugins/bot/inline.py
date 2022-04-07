"""
This Project Under Team-Silent💞 < @SILENT_DEVS >
Orgination Github Of this TeamSilent < https://github.com/TeamSilentt > Check out
Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
Found on github < https://github.com/HYPER-AD17 >
©Team Silent™
"""
import asyncio
from config import Config
from utils import USERNAME
from pyrogram import Client, errors
from youtubesearchpython import VideosSearch
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup

REPLY_MESSAGE=Config.REPLY_MESSAGE

buttons = [
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ🥀", url="t.me/SILENT_DEVS"),
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs💬", url="https://t.me/SILENT_BOTS"),
            ],
            [
                InlineKeyboardButton("ɴᴜʙ🙋‍♀️", url="https://t.me/HYPER_AD13"),
                InlineKeyboardButton("sᴏᴜʀᴄᴇ💫", url="https://github.com/TeamSilentt/SilentRadioPlayer"),
            ],
            [
                InlineKeyboardButton("ʜᴇʟᴘ👩‍💻", callback_data="help"),
                InlineKeyboardButton("ᴄʟᴏsᴇ🗑️", callback_data="close"),
            ]
         ]


@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "silent":
        answers.append(
            InlineQueryResultPhoto(
                title="ᴀʙᴏᴜᴛ ᴅᴇᴠᴜ ʀᴀᴅɪᴏ ᴘʟᴀʏᴇʀ",
                thumb_url="https://telegra.ph/file/00a7f41225be419fade0b.jpg",
                photo_url="https://telegra.ph/file/00a7f41225be419fade0b.jpg",
                caption=f"sɪʟᴇɴᴛ ʀᴀᴅɪᴏ ᴘʟᴀʏᴇʀ ʙʏ ᴛᴇᴀᴍ sɪʟᴇɴᴛ🤔\n\n<b>ᴇxᴄᴜᴛᴇᴅ ʙʏ : <a href="https://github.com/TeamSilentt">ᴛᴇᴀᴍ-sɪʟᴇɴᴛ👩‍💻</a> | <a href="https://github.com/HYPER-AD17">ɴᴜʙ-ʜʏᴘᴇʀ🧚‍♀️</a> \nᴛᴇᴀᴍ-sɪʟᴇɴᴛ</b>",
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text=("✏️ ᴡʀɪᴛᴇ ʏᴏᴜʀ ǫᴜᴇʀʏ ᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ!"),
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=50)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "/splay https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("ᴇʀʀᴏʀ ᴏᴄᴜʀᴇᴅ:ᴛɪᴍᴇᴏᴜᴛ"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
#
