import json
import requests
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message


def get_data(IP):
    url = f"https://ipinfo.io/{IP}/json"
    r = requests.get(url)
    with open(f"./downloads/{IP}.json", "w") as out_file:
        json.dump(r.json(), out_file, indent=4)
    return f"./downloads/{IP}.json"

# get_data("178.80.101.128")


async def ipinfo(bot: Client, event: Message):
    try:
        ip = event.text.split(' ')[1]
        await event.edit(text="Please Wait, **Processing** your Request")
        data = get_data(ip)
        await bot.delete_messages(chat_id=event.chat.id, message_ids=event.id)
        await bot.send_document(document=data, chat_id=event.chat.id)

    except IndexError:
        await event.edit(text="Please provide **IP** as an argument!!")

    except Exception as e:
        await event.edit(text=f"**ERROR** occurred; Please try again later!!\n{str(e)}")
