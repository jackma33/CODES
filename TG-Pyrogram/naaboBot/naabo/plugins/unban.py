from pyrogram import Client
from naabo.utils.mongo import BotDataBase
from pyrogram.types.messages_and_media.message import Message

db = BotDataBase()


async def unban(bot: Client, event: Message):
    id = event.chat.id
    db.removeFromBlacklist(id)
    await event.edit(text="You Are Now Allowed to Message. ✅")
