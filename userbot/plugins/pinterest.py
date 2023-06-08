# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import DeleteHistoryRequest

plugin_category = "utils"

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
    pattern="sosmed(?: |$)(.*)") 
    command=("frwd", plugin_category),
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
        return await eod(event, "`Berikan link tautan pinterest...`")

    xx = await eor(event, "`Processing...`")
    chat = "@SaveAsbot"
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await event.client.send_message(chat, link)
            response = await response
        if response.text.startswith("Forward"):
            await xx.edit("`Mengunggah...`")
        else:
            await xx.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Upload By: {inline_mention(event.sender)}**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client(DeleteHistoryRequest(peer=chat, max_id=0))
            await xx.delete()
