import asyncio, subprocess
import time
from userbot import bot, LOGGER, LOGGER_GROUP
from telethon import events
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from collections import deque

@bot.on(events.NewMessage(outgoing=True, pattern="^.leave$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Group kek!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sar This is Not A Chat`')

@bot.on(events.NewMessage(outgoing=True, pattern="^;__;$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^;__;$"))
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@bot.on(events.NewMessage(outgoing=True, pattern="^.cry$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.cry$"))
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@bot.on(events.NewMessage(outgoing=True, pattern="^.fp$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.fp$"))
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

@bot.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
