import io

import os

import re

import textwrap

from textwrap import wrap


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock

from userbot import Convert, catub

from ..core.logger import logging

from ..core.managers import edit_delete, edit_or_reply

from ..helpers import file_check, fontTest, media_type, process, soft_deEmojify

from ..helpers.utils import get_user_from_event, reply_id 
from telethon.utils import get_display_name

LOGS = logging.getLogger(__name__)

plugin_category = "fun"




@catub.cat_cmd(
    pattern="sosmed(?:\s|$)([\s\S]*)",
    command=("sosmed", plugin_category),
    info={
        "header": "download TIKTOK, pinterest, Instagram",
        "usage": "{tr}sosmed",
    },
)
async def _(event):
    "download sosmed"
    reply_to = await reply_id(event)
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    message = ""
    messages_id = []
    if reply and input_str and input_str.isnumeric():
        messages_id.append(reply.id)
        async for message in event.client.iter_messages(
            event.chat_id,
            limit=(int(input_str) - 1),
            offset_id=reply.id,
            reverse=True,
        ):
            if message.id != event.id:
                messages_id.append(message.id)
    elif (
        reply
        and (not input_str or not input_str.isnumeric())
        and input_str
        or not reply
        and input_str
    ):
        message = input_str
    elif reply and (not input_str or not input_str.isnumeric()) and not input_str:
        messages_id.append(reply.id)
    else:
        return await edit_delete(
            event, "`Either reply to message or give input to function properly`"
        )
    chat = "@SaveAsbot"
    catevent = await edit_or_reply(event, "```processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
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
            await event.client(UnblockRequest(chat))

            await event.client.send_message(chat, link)

            response = await response

        if response.text.startswith("Forward"):

            await catevent.edit("`Mengunggah...`")

        else:

            await catevent.delete()

            await event.client.send_file(

                event.chat_id,

                response.message.media,

                

            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await catevent.delete()
            await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_to
        )
            
