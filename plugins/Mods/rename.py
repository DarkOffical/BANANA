
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import humanize
from info import ADMINS , FLOOD, RENAME_MODE
import random


@Client.on_message( filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    if (RENAME_MODE==True):
        if message.from_user.id in ADMINS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n**ᴩʟᴇᴀꜱᴇ ᴛᴇʟʟ, ᴡʜᴀᴛ ꜱʜᴏᴜʟᴅ ɪ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴", callback_data="rename") ],
                       [ InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))

        elif message.from_user.id in ADMINS
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            try:
                text = f"""\n**ᴩʟᴇᴀꜱᴇ ᴛᴇʟʟ, ᴡʜᴀᴛ ꜱʜᴏᴜʟᴅ ɪ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴", callback_data="rename") ],
                           [ InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
                await sleep(FLOOD)
            except FloodWait as e:
                await sleep(e.value)
                text = f"""\n**ᴩʟᴇᴀꜱᴇ ᴛᴇʟʟ, ᴡʜᴀᴛ ꜱʜᴏᴜʟᴅ ɪ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙸𝙽𝙶", callback_data="rename") ],
                           [ InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
            except:
                pass
        else:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n**ᴩʟᴇᴀꜱᴇ ᴛᴇʟʟ, ᴡʜᴀᴛ ꜱʜᴏᴜʟᴅ ɪ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙸𝙽𝙶", callback_data="requireauth") ],
                        [ InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return
