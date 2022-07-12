from pyrogram import Client
from pyrogram.types.messages_and_media.message import Message


async def start(bot: Client, event: Message):
    info = event.from_user
    id = info.id
    name = info.first_name

    await event.edit(text=f"Hi, {name}\nID: {id}")
