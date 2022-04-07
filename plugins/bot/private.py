"""
This Project Under Team-Silent💞 < @SILENT_DEVS >
Orgination Github Of this TeamSilent < https://github.com/TeamSilentt > Check out
Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
Found on github < https://github.com/HYPER-AD17 >
©Team Silent™
"""
import asyncio
from config import Config
from utils import USERNAME, mp
from pyrogram import Client, filters, emoji
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

msg=Config.msg
ADMINS=Config.ADMINS
CHAT_ID=Config.CHAT_ID
playlist=Config.playlist
LOG_GROUP=Config.LOG_GROUP

HOME_TEXT = "👋🏻 **ʜᴇʟʟᴏ [{}](tg://user?id={})**,\n\nɪ ᴍ **sɪʟᴇɴᴛ ʀᴀᴅɪᴏ sᴛʀᴇᴀᴍᴇʀ** \nɪ ᴄᴀɴ ᴘʟᴀʏ ʀᴀᴅɪᴏ / ᴍᴜsɪᴄ / ʏᴏᴜᴛᴜʙᴇ ʟɪᴠᴇ ɪɴ ᴄʜᴀɴɴᴇʟ & ɢʀᴏᴜᴘ 24x7 ɴᴏɴsᴛᴏᴘ. ᴍᴀᴅᴇ ᴡɪᴛʜ 👩‍💻 ʙʏ ᴛᴇᴀᴍ-sɪʟᴇɴᴛ 🧚‍♀️!"
HELP_TEXT = """
💡 --**sᴇᴛᴛɪɴɢ ʀᴀᴅɪᴏ ʀᴏʙᴏ**--:

\n✦ `ᴀᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.`
\n✦ `sᴛᴀʀᴛ ᴀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ & ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ɪꜰ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴠᴄ.`
\n✦ `ᴜsᴇ` /splay `[sᴏɴɢ ɴᴀᴍᴇ] ᴏʀ ᴜsᴇ` /splay `ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ.`

💡 --**ᴄᴏᴍᴍᴏɴ ᴜsᴇʀ ᴄᴍᴅs**--:

\n✦ /help - `sʜᴏᴡs ʜᴇʟᴘ ꜰᴏʀ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs`
\n✦ /song [sᴏɴɢ ɴᴀᴍᴇ] - `ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ sᴏɴɢ ᴀs ᴀᴜᴅɪᴏ​`
\n✦ /current - `sʜᴏᴡs ᴄᴜʀʀᴇɴᴛ ᴛʀᴀᴄᴋ ᴡɪᴛʜ ᴄᴏɴᴛʀᴏʟs`​
\n✦ /playlist - `sʜᴏᴡs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ & ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ​`

💡 --**ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs**--:

\n✦ /radio - `sᴛᴀʀᴛ ʀᴀᴅɪᴏ.`
\n✦ /stopradio - `sᴛᴏᴘ ʀᴀᴅɪᴏ.`
\n✦ /next - `ᴍᴏᴠᴇ ᴛᴏ ɴᴇxᴛ sᴏɴɢ.`
\n✦ /joinvc - `ᴊᴏɪɴ ᴠᴄ ᴄʜᴀᴛ.`
\n✦ /leavevc - `ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.`
\n✦ /end - `ᴇɴᴅ ᴘʟᴀʏʙᴀᴄᴋ`
\n✦ /vol - `ᴄʜᴀɴɢᴇ ᴠᴏʟᴜᴍᴇ (0-200)`
\n✦ /rplay - `ᴘʟᴀʏ ғʀᴏᴍ sᴛᴀʀᴛɪɴɢ`
\n✦ /rms - `ᴄʟᴇᴀʀ ᴄᴘᴜ ᴏғ ʙᴏᴛ`
\n✦ /pause - `ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ`
\n✦ /resume - `ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ`
\n✦ /pmute - `ᴍᴜᴛᴇ ᴀssɪsᴛᴇɴᴛ`
\n✦ /punmute - `ᴜɴᴍᴜᴛᴇ ᴀssɪsᴛᴇɴᴛ`
\n✦ /restart - `ʀᴇsᴛᴀʀᴛ ʀᴏʙᴏᴛ`

`➬➬ Pᴏᴡᴇʀᴇᴅ Bʏ Cᴏɴᴛʀᴏʟʟᴇʀ Tᴇᴀᴍ-Sɪʟᴇɴᴛ💞`
 @SILENT_DEVS ✨,
"""

# \u066D /setvar - `ᴄʜᴀɴɢᴇ ʜᴇʀᴏᴋᴜ ᴄᴏɴғɪɢ/ᴠᴀʀs`

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.from_user.id not in Config.ADMINS and query.data != "help":
        await query.answer(
            "ʟᴀʟᴀ ᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪᴛɪᴏɴ",
            show_alert=True
            )
        return

    if query.data.lower() == "rplay":
        group_call = mp.group_call
        if not playlist:
            await query.answer("⛔️ ᴘʟᴀʏʟɪsᴛ ᴇᴍᴘᴛʏ !", show_alert=True)
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} **ᴘʟᴀʏʟɪsᴛ ᴇᴍᴘᴛʏ**"
        else:
            pl = f"{emoji.PLAY_BUTTON} **ᴘʟᴀʏʟɪsᴛ**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **ʀᴇǫᴜᴇsᴛᴇʀ:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.answer("✅ ʀᴇᴘʟʏɪɴɢ !", show_alert=True)
            await query.edit_message_text(f"{pl}",
                    parse_mode="Markdown",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔄", callback_data="rplay"),
                                InlineKeyboardButton("⏸", callback_data="pause"),
                                InlineKeyboardButton("⏩", callback_data="next")
                            ],
                        ]
                    )
                )
        except MessageNotModified:
            pass

    elif query.data.lower() == "pause":
        if not playlist:
            await query.answer("⛔️ ᴘʟᴀʏʟɪsᴛ ᴇᴍᴘᴛʏ !", show_alert=True)
            return
        else:
            mp.group_call.pause_playout()
            pl = f"{emoji.PLAY_BUTTON} **ᴘʟᴀʏʟɪsᴛ**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  **ʀᴇǫᴜᴇsᴛᴇʀ:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.answer("⏸ ᴘᴀᴜsᴇᴅ !", show_alert=True)
            await query.edit_message_text(f"{pl}",
                    parse_mode="Markdown",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔄", callback_data="rplay"),
                                InlineKeyboardButton("▶️", callback_data="resume"),
                                InlineKeyboardButton("⏩", callback_data="next")
                            ],
                        ]
                    )
                )
        except MessageNotModified:
            pass

    elif query.data.lower() == "resume":   
        if not playlist:
            await query.answer("⛔️ ᴘʟᴀʏʟɪsᴛ ᴇᴍᴘᴛʏ !", show_alert=True)
            return
        else:
            mp.group_call.resume_playout()
            pl = f"{emoji.PLAY_BUTTON} **ᴘʟᴀʏʟɪsᴛ**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **ʀᴇǫᴜᴇsᴛᴇʀ:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.answer("▶️ ʀᴇsᴜᴍᴇᴅ !", show_alert=True)
            await query.edit_message_text(f"{pl}",
                    parse_mode="Markdown",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔄", callback_data="rplay"),
                                InlineKeyboardButton("⏸", callback_data="pause"),
                                InlineKeyboardButton("⏩", callback_data="next")
                            ],
                        ]
                    )
                )
        except MessageNotModified:
            pass

    elif query.data.lower() == "next":   
        if not playlist:
            await query.answer("⛔️ ᴘʟᴀʏʟɪsᴛ ᴇᴍᴘᴛʏ !", show_alert=True)
            return
        else:
            await mp.skip_current_playing()
            pl = f"{emoji.PLAY_BUTTON} **ᴘʟᴀʏʟɪsᴛ**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **ʀᴇǫᴜᴇsᴛᴇʀ:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.answer("⏩ ᴍᴏᴠᴇᴅ ᴛᴏ ɴᴇxᴛ !", show_alert=True)
            await query.edit_message_text(f"{pl}",
                    parse_mode="Markdown",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔄", callback_data="rplay"),
                                InlineKeyboardButton("⏸", callback_data="pause"),
                                InlineKeyboardButton("⏩", callback_data="next")
                            ],
                        ]
                    )
                )
        except MessageNotModified:
            pass

    elif query.data.lower() == "help":
        buttons = [      
            [
                InlineKeyboardButton("ᴛᴇᴀᴍ-sɪʟᴇɴᴛ🧚‍♀️", url="https://t.me/SILENT_DEVS"),
                InlineKeyboardButton("ɢᴏ ɪɴʟɪɴᴇ👩‍💻", switch_inline_query_current_chat=""),
            ],           
            [
                InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ💁‍♂️", callback_data="home"),
                InlineKeyboardButton("ᴄʟᴏsᴇ🗑️", callback_data="close"),
            ],
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data.lower() == "home":
        buttons = [
            [
                InlineKeyboardButton("ᴛᴇᴀᴍ-sɪʟᴇɴᴛ🧚‍♀️", url="https://t.me/SILENT_DEVS"),
                InlineKeyboardButton("ɢᴏ ɪɴʟɪɴᴇ👩‍💻", switch_inline_query_current_chat=""),
            ],
            [
                InlineKeyboardButton("ʜᴇʟᴘ ɴᴅ ᴄᴏᴍᴍᴀɴᴅs💫", callback_data="help"),
            ],
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data.lower() == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

    await query.answer()



@Client.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("ᴛᴇᴀᴍ-sɪʟᴇɴᴛ🧚‍♀️", url="https://t.me/SILENT_DEVS"),
                InlineKeyboardButton("ɢᴏ ɪɴʟɪɴᴇ👩‍💻", switch_inline_query_current_chat=""),
            ],
            [
                InlineKeyboardButton("ʜᴇʟᴘ ɴᴅ ᴄᴏᴍᴍᴀɴᴅs💫", callback_data="help"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply_photo(photo="https://telegra.ph/file/00a7f41225be419fade0b.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)


@Client.on_message(filters.command(["help", f"help@{USERNAME}"]))
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("ᴛᴇᴀᴍ-sɪʟᴇɴᴛ🧚‍♀️", url="https://t.me/SILENT_DEVS"),
                InlineKeyboardButton("ɢᴏ ɪɴʟɪɴᴇ👩‍💻", switch_inline_query_current_chat=""),
            ],           
            [
                InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ💁‍♂️", callback_data="home"),
                InlineKeyboardButton("ᴄʟᴏsᴇ🗑️", callback_data="close"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_photo(photo="https://telegra.ph/file/00a7f41225be419fade0b.jpg", caption=HELP_TEXT, reply_markup=reply_markup)
    await mp.delete(message)


@Client.on_message(filters.command(["setvar", f"setvar@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private | filters.chat(LOG_GROUP)))
async def set_heroku_var(client, message):
    if not Config.HEROKU_APP:
        buttons = [[InlineKeyboardButton('HEROKU_API_KEY', url='https://dashboard.heroku.com/account/applications/authorizations/new')]]
        k=await message.reply_text(
            text="❗ **No Heroku App Found !** \n__Please Note That, This Command Needs The Following Heroku Vars To Be Set :__ \n\n1. `HEROKU_API_KEY` : Your heroku account api key.\n2. `HEROKU_APP_NAME` : Your heroku app name. \n\n**For More Ask In @AsmSupport !!**", 
            reply_markup=InlineKeyboardMarkup(buttons))
        await mp.delete(k)
        await mp.delete(message)
        return
    if " " in message.text:
        cmd, env = message.text.split(" ", 1)
        if  not "=" in env:
            k=await message.reply_text("❗ **You Should Specify The Value For Variable!** \n\nFor Example: \n`/setvar CHAT_ID=-1001313215676`")
            await mp.delete(k)
            await mp.delete(message)
            return
        var, value = env.split("=", 2)
        config = Config.HEROKU_APP.config()
        if not value:
            m=await message.reply_text(f"❗ **No Value Specified, So Deleting `{var}` Variable !**")
            await asyncio.sleep(2)
            if var in config:
                del config[var]
                await m.edit(f"🗑 **Sucessfully Deleted `{var}` !**")
                config[var] = None
            else:
                await m.edit(f"🤷‍♂️ **Variable Named `{var}` Not Found, Nothing Was Changed !**")
            return
        if var in config:
            m=await message.reply_text(f"⚠️ **Variable Already Found, So Edited Value To `{value}` !**")
        else:
            m=await message.reply_text(f"⚠️ **Variable Not Found, So Setting As New Var !**")
        await asyncio.sleep(2)
        await m.edit(f"✅ **Succesfully Set Variable `{var}` With Value `{value}`, Now Restarting To Apply Changes !**")
        config[var] = str(value)
        await mp.delete(m)
        await mp.delete(message)
        return
    else:
        k=await message.reply_text("❗ **You Haven't Provided Any Variable, You Should Follow The Correct Format !** \n\nFor Example: \n• `/setvar CHAT_ID=-1001313215676` to change or set CHAT var. \n• `/setvar REPLY_MESSAGE=` to delete REPLY_MESSAGE var.")
        await mp.delete(k)
        await mp.delete(message)
