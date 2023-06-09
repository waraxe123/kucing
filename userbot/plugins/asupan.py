


from secrets import choice

from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterVideo

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply

plugin_category="fun"

from . import *


@catub.cat_cmd(
    pattern="asupan(?:\s|$)([\s\S]*)",
    command=("asupan", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "cokbun ae lu kontol",
        "usage": "{tr}asupan <text>",
        "examples": "{tr}asupan how are you doing",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@punyakenkan", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=choice(asupannya),
            reply_to=event.reply_to_msg_id,
            
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")


@catub.cat_cmd(
    pattern="bokep(?:\s|$)([\s\S]*)",
    command=("bokep", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "cokbun ae lu kontol",
        "usage": "{tr}bokep <text>",
        "examples": "{tr}bokep ",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        bokepnya = [
            bokep
            async for bokep in event.client.iter_messages(
                "@bahaninimah", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=choice(bokepnya),
            reply_to=event.reply_to_msg_id,
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan bokep.**")


@catub.cat_cmd(
    pattern="ayang(?:\s|$)([\s\S]*)",
    command=("ayang", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "ayang ae lu kontol",
        "usage": "{tr}ayang <text>",
        "examples": "{tr}ayang ",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=choice(ayangnya),
            reply_to=event.reply_to_msg_id,
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan ayang.**")


@catub.cat_cmd(
    pattern="ppcp(?:\s|$)([\s\S]*)",
    command=("ppcp", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "ppcp ae lu kontol",
        "usage": "{tr}ppcp <text>",
        "examples": "{tr}ppcp ",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        ppcpnya = [
            ppcp
            async for ppcp in event.client.iter_messages(
                "@ppcpcilik", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ppcpnya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan ppcp.**")


@catub.cat_cmd(
    pattern="ppcp2(?:\s|$)([\s\S]*)",
    command=("ppcp2", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "ppcp2 ae lu kontol",
        "usage": "{tr}ppcp2 <text>",
        "examples": "{tr}ppcp2 ",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        ajgg = [
            gg
            async for gg in event.client.iter_messages(
                "@mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ajgg), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan ppcp2.**")


@catub.cat_cmd(
    pattern="anime(?:\s|$)([\s\S]*)",
    command=("anime", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "anime ae lu kontol",
        "usage": "{tr}anime <text>",
        "examples": "{tr}anime ",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        nimek = [
            nime
            async for nime in event.client.iter_messages(
                "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(nimek), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan anime.**")


@catub.cat_cmd(
    pattern="anime2(?:\s|$)([\s\S]*)",
    command=("anime2", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "anime2 ae lu kontol",
        "usage": "{tr}anime2 <text>",
        "examples": "{tr}anime2 ",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        nimekk = [
            nim
            async for nim in event.client.iter_messages(
                "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(nimekk), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan anime2.**")


@catub.cat_cmd(
    pattern="pap(?:\s|$)([\s\S]*)",
    command=("pap", plugin_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "pap ae lu kontol",
        "usage": "{tr}pap <text>",
        "examples": "{tr}pap ",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        papjing = [
            jinglu
            async for jinglu in event.client.iter_messages(
                "@mm_kyran", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(papjing), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cowo.**")
