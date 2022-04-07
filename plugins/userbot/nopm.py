"""
This Project Under Team-Silent💞 < @SILENT_DEVS >
Orgination Github Of this TeamSilent < https://github.com/TeamSilentt > Check out
Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
Found on github < https://github.com/HYPER-AD17 >
©Team Silent™
"""

import asyncio
from pyrogram import Client, filters
from utils import USERNAME
from config import Config
from pyrogram.errors import BotInlineDisabled

msg=Config.msg
REPLY_MESSAGE=Config.REPLY_MESSAGE

@Client.on_message(filters.private & filters.incoming & ~filters.bot & ~filters.service & ~filters.me & ~filters.edited & ~filters.chat([777000, 454000]))
async def nopm(client, message): 
    try:
        inline = await client.get_inline_bot_results(USERNAME, "SAF_ONE")
        m=await client.send_inline_bot_result(
            message.chat.id,
            query_id=inline.query_id,
            result_id=inline.results[0].id,
            hide_via=True
            )
        old=msg.get(message.chat.id)
        if old:
            await client.delete_messages(message.chat.id, [old["msg"], old["s"]])
        msg[message.chat.id]={"msg":m.updates[1].message.id, "s":message.message_id}
    except BotInlineDisabled:
            print(f"Inline Mode for @{USERNAME} is not enabled. Enable it from @Botfather to turn on PM Guard !")
            await message.reply_text(f"{REPLY_MESSAGE}\n\n<b> ➬➬ Pᴏᴡᴇʀᴇᴅ Bʏ Cᴏɴᴛʀᴏʟʟᴇʀ Tᴇᴀᴍ-Sɪʟᴇɴᴛ💞</b>")
    except Exception as e:
        print(e)
        pass
