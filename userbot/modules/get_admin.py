from telethon import TelegramClient, events
from telethon.errors import ChatAdminRequiredError
from telethon.tl.types import ChannelParticipantsAdmins, ChatParticipantCreator, Chat

from userbot import bot

<<<<<<< HEAD
@bot.on(events.NewMessage(pattern="^.admemelist (.*)", outgoing=True))
async def get_admin(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        mentions = "**Admins in this Chat**: \n"
        choice = int(e.pattern_match.group(1))
        to_write_chat = LOGGER_GROUP
        chat = None
        mentions = "Admins in channel {}: \n".format(str(e.chat_id))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.adminlist"))
async def get_admin(show):
    if not show.text[0].isalpha() and show.text[0] not in ("/", "#", "@", "!"):
        mentions = "Admins in {}: \n".format(show.chat.title or "this chat")
>>>>>>> 1ce4916... [REFACTOR] : Linting the stuff (1)
        try:
            async for user in bot.iter_participants(
                show.chat_id, filter=ChannelParticipantsAdmins
            ):
                if not user.deleted:
                    mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
        except ChatAdminRequiredError as ea:
            mentions += " " + str(ea) + "\n"
        await show.edit(mentions)