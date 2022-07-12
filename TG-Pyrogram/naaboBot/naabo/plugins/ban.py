from pyrogram import Client
from naabo.utils.mongo import BotDataBase
from pyrogram.types.messages_and_media.message import Message

db = BotDataBase()


async def ban(bot: Client, event: Message):
    id = event.chat.id
    db.addToBlackList(id)
    await event.edit(text="❌ You Are Banned!! ❌")
