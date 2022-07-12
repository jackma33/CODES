from pyrogram import Client
from pyrogram.types.messages_and_media.message import Message


async def MessageHandler(bot: Client, event: Message):
    await event.reply(text="Hey")
