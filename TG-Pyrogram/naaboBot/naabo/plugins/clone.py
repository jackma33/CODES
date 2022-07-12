from pyrogram import Client
from pyrogram.types.messages_and_media.message import Message


async def clone(bot: Client, event: Message):
    try:
        userDetails = event.reply_to_message.from_user
        user = await bot.get_chat(userDetails.id)
    except:
        userDetails = event.chat
        user = await bot.get_chat(userDetails.id)

    userProfilePic = await bot.download_media(message=user.photo.small_file_id)
    await bot.set_profile_photo(photo=userProfilePic)
    # await bot.update_profile(first_name=user.first_name, last_name=user.last_name, bio=user.bio)
