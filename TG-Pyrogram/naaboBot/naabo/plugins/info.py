from pyrogram import Client
from pyrogram.types.messages_and_media.message import Message


async def info(bot: Client, event: Message):
    try:
        info = event.reply_to_message.from_user
        id = event.chat.id
    except:
        info = event.chat
        id = info.id

    try:
        profile_pic = await bot.download_media(message=info.photo.big_file_id, file_name="./downloads/profil_pic.jpg")
        await bot.send_photo(caption=info, chat_id=id, photo=profile_pic)
    except:
        await bot.send_message(chat_id=id, text=info)
