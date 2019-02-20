<<<<<<< HEAD
import sqlite3
import time

from telethon import TelegramClient, events
from telethon.errors import (ChannelInvalidError, ChatAdminRequiredError,
                             UserAdminInvalidError)
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights
=======
from time import sleep

from telethon import events
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest

from telethon.tl.types import ChatAdminRights, ChatBannedRights

from userbot import (BRAIN_CHECKER, LOGGER, LOGGER_GROUP, bot)
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61

from userbot import (BRAIN_CHECKER, LOGGER, LOGGER_GROUP, SPAM, SPAM_ALLOWANCE,
                     bot)

<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern="^.upromote$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.upromote$"))
async def wizzard(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        chats=await e.get_chat()
        rights = chats.admin_rights
        rights3 = chats.creator
        rights2 = ChatAdminRights(
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.promote$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.promote$"))
async def promote(promt):
    """ For .promote command, do promote targeted person """
    if not promt.text[0].isalpha() \
            and promt.text[0] not in ("/", "#", "@", "!"):
        chats = await promt.get_chat()
        admin = chats.admin_rights
        creator = chats.creator
        new_rights = ChatAdminRights(
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            add_admins=True,
            invite_users=True,
            change_info=True,
            ban_users=True,
            delete_messages=True,
            pin_messages=True
        )

        # Self explanatory
        if not await promt.get_reply_message():
            await promt.edit("`Give a reply message`")
        elif not admin and creator:
            rights = new_rights
        elif not admin and not creator:
            rights = None
        await promt.edit("`Promoting...`")

        # Try to promote if current user is admin or creator
        try:
            await bot(
                EditAdminRequest(promt.chat_id,
                                 (await promt.get_reply_message()).sender_id,
                                 rights)
            )
<<<<<<< HEAD
        except Exception:
            await e.edit("`You Don't have sufficient permissions to paramod`")
=======

        # If Telethon spit BadRequestError, assume
        # we don't have Promote permission
        except BadRequestError:
            await promt.edit(
                "`You Don't have sufficient permissions to parmod`"
                )
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            return
        await promt.edit("`Promoted Successfully!`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.demote$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.demote$"))
<<<<<<< HEAD
async def demote(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        rights = ChatAdminRights(
            add_admins=False,
            invite_users=False,
            change_info=False,
            ban_users=False,
            delete_messages=False,
            pin_messages=False,
            invite_link=False,
        )
        chat=await e.get_chat()
        rights = chat.admin_rights
        rights2 = chat.creator
        if not (await e.get_reply_message()):
            await e.edit("`Give a reply message`")
=======
async def demote(dmod):
    """ For .demote command, do demote targeted person """
    if not dmod.text[0].isalpha() and dmod.text[0] not in ("/", "#", "@", "!"):
        # Get targeted chat
        chat = await dmod.get_chat()
        # Grab admin status or creator in a chat
        admin = chat.admin_rights
        creator = chat.creator

        # If there's no reply, return
        if not await dmod.get_reply_message():
            await dmod.edit("`Give a reply message`")
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            return
        # If not admin and not creator, also return
        if not admin and not creator:
            await dmod.edit("`You aren't an admin!`")
            return

        # If passing, declare that we're going to demote
        await dmod.edit("`Demoting...`")

        # New rights after demotion
        newrights = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None
        )
        # Edit Admin Permission
        try:
            await bot(
                EditAdminRequest(dmod.chat_id,
                                 (await dmod.get_reply_message()).sender_id,
                                 newrights)
            )
<<<<<<< HEAD
        except Exception:
            await e.edit("`You Don't have sufficient permissions to demhott`")
=======

        # If we catch BadRequestError from Telethon
        # Assume we don't have permission to demote
        except BadRequestError:
            await dmod.edit("`You Don't have sufficient permissions to demhott`")
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            return
        await dmod.edit("`Demoted Successfully!`")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern="^.uban$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.uban$"))
async def thanos(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        rights = ChatBannedRights(
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.ban$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.ban$"))
async def thanos(bon):
    """ For .ban command, do "thanos" at targeted person """
    if not bon.text[0].isalpha() and bon.text[0] not in ("/", "#", "@", "!"):
        banned_rights = ChatBannedRights(
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            until_date=None,
            view_messages=True,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
        )

        # Here laying the sanity check
        chat = await bon.get_chat()
        admin = chat.admin_rights
        creator = chat.creator

        # For dealing with reply-at-ban
        sender = await bon.get_reply_message()

        # Well
        if not admin and not creator:
            await bon.edit("`You aren't an admin!`")
            return

        # If the user is a sudo
        try:
            if sender.sender_id in BRAIN_CHECKER:
                await bon.edit("`Ban Error! I am not supposed to ban this user`")
                return

        # This exception handled if the user doesn't
        # Specifying any target (reply in this case)
        except AttributeError:
            await bon.edit("`You don't seems to do this right`")
            return

        # Announce that we're going to whacking the pest
        await bon.edit("`Whacking the pest!`")
        await bot(
            EditBannedRequest(
                bon.chat_id,
                sender.sender_id,
                banned_rights
            )
        )

        # Delete message and then tell that the command
        # is done gracefully
        await bon.edit("`Banned!`")

        # Announce to the logging group if we done a banning
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await bon.get_reply_message()).sender_id) + " was banned.",
            )

@bot.on(events.NewMessage(outgoing=True, pattern="^.unban$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.unban$"))
async def nothanos(unbon):
    if not unbon.text[0].isalpha() and unbon.text[0] not in ("/", "#", "@", "!"):
        rights = ChatBannedRights(
            until_date=None,
            send_messages=None,
            send_media=None,
            send_stickers=None,
            send_gifs=None,
            send_games=None,
            send_inline=None,
            embed_links=None,
            )
        replymsg = await unbon.get_reply_message()
        try:
            await bot(EditBannedRequest(
                unbon.chat_id,
                replymsg.sender_id,
                rights
                ))
            await unbon.edit("```Unbanned Successfully```")

            if LOGGER:
                await bot.send_message(
                    LOGGER_GROUP,
                    str((await unbon.get_reply_message()).sender_id) + " was unbanned.",
                )
        except UserIdInvalidError:
            await unbon.edit("`Uh oh my unban logic broke!`")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern="^.umute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.umute$"))
async def spider(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if (await e.get_reply_message()).sender_id in BRAIN_CHECKER:
            await e.edit("`Mute Error! I am not supposed to mute this user`")
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.mute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.mute$"))
async def spider(spdr):
    """
    This function basically muting peeps
    """
    if not spdr.text[0].isalpha() and spdr.text[0] not in ("/", "#", "@", "!"):

        # If the targeted user is a Sudo
        if (await spdr.get_reply_message()).sender_id in BRAIN_CHECKER:
            await spdr.edit("`Mute Error! I am not supposed to mute this user`")
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            return

        # Check if the function running under SQL mode
        try:
            from userbot.modules.sql_helper.spam_mute_sql import mute
        except Exception:
<<<<<<< HEAD
            await e.edit("`Running on Non-SQL mode!`")
=======
            await spdr.edit("`Running on Non-SQL mode!`")
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            return

        # Get the targeted chat
        chat = await spdr.get_chat()
        # Check if current user is admin
        admin = chat.admin_rights
        # Check if current user is creator
        creator = chat.creator

        # If not admin and not creator, return
        if not admin and not creator:
            await spdr.edit("`You aren't an admin!`")
            return

        target = await spdr.get_reply_message()
        # Else, do announce and do the mute
        mute(spdr.chat_id, target.sender_id)
        await spdr.edit("`Gets a tape!`")

        # Announce that the function is done
        await spdr.edit("`Safely taped!`")

        # Announce to logging group
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await spdr.get_reply_message()).sender_id)
                + " was muted.",
            )

<<<<<<< HEAD

@bot.on(events.NewMessage(incoming=True, pattern="<triggerban>"))
async def triggered_ban(e):
    ban_id = int(e.text[13:])
    if e.sender_id in BRAIN_CHECKER:  # non-working module#
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
        )
    if ban_id in BRAIN_CHECKER:
        await e.edit("`Sorry Master!`")
        return
    await e.edit("`Command from my Master!`")
    time.sleep(5)
    await bot(EditBannedRequest(e.chat_id, ban_id, rights))
    await e.delete()
    await bot.send_message(e.chat_id, "Job was done, Master! Gimme Cookies!")


=======
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
@bot.on(events.NewMessage(outgoing=True, pattern="^.unmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.unmute$"))
async def unmoot(unmot):
    if not unmot.text[0].isalpha() and unmot.text[0] not in ("/", "#", "@", "!"):
        rights = ChatBannedRights(
            until_date=None,
            send_messages=None,
            send_media=None,
            send_stickers=None,
            send_gifs=None,
            send_games=None,
            send_inline=None,
            embed_links=None,
            )
        replymsg = await unmot.get_reply_message()
        from userbot.modules.sql_helper.spam_mute_sql import unmute
        unmute(unmot.chat_id, replymsg.sender_id)
        try:
            await bot(EditBannedRequest(
                unmot.chat_id,
                replymsg.sender_id,
                rights
                ))
            await unmot.edit("```Unmuted Successfully```")
        except UserIdInvalidError:
            await unmot.edit("`Uh oh my unmute logic broke!`")


@bot.on(events.NewMessage(incoming=True))
@bot.on(events.MessageEdited(incoming=True))
async def muter(moot):
    try:
        from userbot.modules.sql_helper.spam_mute_sql import is_muted
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
    except:
        return
    muted = is_muted(moot.chat_id)
    gmuted = is_gmuted(moot.sender_id)
    rights = ChatBannedRights(
                until_date=None,
                send_messages=True,
                send_media=True,
                send_stickers=True,
                send_gifs=True,
                send_games=True,
                send_inline=True,
                embed_links=True,
                )
    if muted:
        for i in muted:
            if str(i.sender) == str(moot.sender_id):
                await moot.delete()
                await bot(EditBannedRequest(
                    moot.chat_id,
                    moot.sender_id,
                    rights
                    ))
    for i in gmuted:
        if i.sender == str(moot.sender_id):
            await moot.delete()


@bot.on(events.NewMessage(outgoing=True, pattern="^.ungmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.ungmute$"))
<<<<<<< HEAD
async def ungmute(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
=======
async def ungmoot(ungmoot):
    if not ungmoot.text[0].isalpha() and ungmoot.text[0] \
            not in ("/", "#", "@", "!"):
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            await ungmoot.edit('`Running on Non-SQL Mode!`')
        ungmute(str((await ungmoot.get_reply_message()).sender_id))
        await ungmoot.edit("```Ungmuted Successfully```")


@bot.on(events.NewMessage(outgoing=True, pattern="^.gmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.gmute$"))
<<<<<<< HEAD
async def gmute(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if (await e.get_reply_message()).sender_id in BRAIN_CHECKER:
            await e.edit("`Mute Error! Couldn't mute this user`")
=======
async def gspider(gspdr):
    if not gspdr.text[0].isalpha() and gspdr.text[0] not in ("/", "#", "@", "!"):
        if (await gspdr.get_reply_message()).sender_id in BRAIN_CHECKER:
            await gspdr.edit("`Mute Error! Couldn't mute this user`")
>>>>>>> bb043a4e9d013d23ca853b453a9602df1b128f61
            return
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except Exception as err:
            print(err)
            await gspdr.edit("`Running on Non-SQL mode!`")
            return

        gmute(str((await gspdr.get_reply_message()).sender_id))
        await gspdr.edit("`Grabs a huge, sticky duct tape!`")
        sleep(5)
        await gspdr.delete()
        await gspdr.respond("`Taped!`")

        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await gspdr.get_reply_message()).sender_id)
                + " was muted.",
            )
