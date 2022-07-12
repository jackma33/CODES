from pyrogram import Client
from pyrogram.types.messages_and_media.message import Message


async def start(bot: Client, event: Message):
    await event.reply(text=f"Welcome, {event.chat.first_name}")
