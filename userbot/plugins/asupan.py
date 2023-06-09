


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


@ayra_cmd(pattern="[Bb][o][k][e][p]$")
async def _(event):
    if event.chat_id in NOSPAM_CHAT:
        return await eor(event, "**Perintah ini Dilarang digunakan di Group ini**")
    xx = await eor(event, "`Tunggu Sebentar...`")
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
            caption=f"**Coli Mulu {inline_mention(event.sender)}..**",
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan bokep.**")


@ayra_cmd(pattern="[Aa][y][a][n][g]$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
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
            caption=f"**Ayang Nya {inline_mention(event.sender)}..**",
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan ayang.**")


@ayra_cmd(pattern="(ppcp|Ppcp)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
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


@ayra_cmd(pattern="(Ppcp2|ppcp2)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
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


@ayra_cmd(pattern="(Anime|anime)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
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


@ayra_cmd(pattern="(anime2|Anime2)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
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


@ayra_cmd(pattern="(pap|Pap)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
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
