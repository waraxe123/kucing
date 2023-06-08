# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import DeleteHistoryRequest

try:
    import cv2
except ImportError:
    cv2 = None

try:
    from htmlwebshot import WebShot
except ImportError:
    WebShot = None

from . import *


@catub.cat_cmd(
    pattern="sosmed(?:\s|$)([\s\S]*)",
    command=("sosmed", plugin_category),
    info={
        "header": "To get view counter for the message. that is will delete old message and send new message where you can see how any people saw your message",
        "usage": "{tr}sosmed",
    },
)
async def pntr(event):
    if xxnx := event.pattern_match.group(1):
        link = xxnx
    elif event.is_reply:
        link = await event.get_reply_message()
    else:
        return await edit_delete(event, "`Berikan link tautan pinterest...`")

    xx = await event.edit("`Processing..`")
    chat = "@SaveAsbot"
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            if messages_id != []:
                await event.client.forward_messages(chat, messages_id, event.chat_id)
            elif message != "":
                await event.client.send_message(conv.chat_id, message)
            else:
                return await edit_delete(
                    catevent, "`I guess you have used a invalid syntax`"
                )
            response = await response
        except YouBlockedUserError:
            return await catevent.edit("```Please unblock me (@SaveAsbot) u Nigga```")
        await event.client.send_read_acknowledge(conv.chat_id)
        await catevent.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_to
            
            
        