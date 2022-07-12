from time import sleep
from naabo import Config
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

app = Client("my_account",
             api_id=15918522,
             api_hash="689382b9f19dbc03d0dd12ce157438dc",
             session_string=Config.stringSession)


def slmi(id):
    with open('latest-m-id', 'w') as f:
        f.write(str(id))
    print(f"Message ID: {id}")


m = []


@app.on_message(filters.command(['now', 'after'], prefixes=['You can send new task']) & filters.bot)
async def Handler(bot: Client, event: Message):
    print(1)
    if event.chat.id == 948320744:
        slmi(event.id)
        n = event.id
        if "after" not in event.text.lower():
            async for message in app.get_chat_history(-1001704658427):
                m.append(message)
            if len(m) != 0:
                await app.forward_messages(948320744, -1001704658427, m[0].id)
                await app.delete_messages(-1001704658427, m[0].id)
                m.pop(0)


@app.on_message(filters.text & filters.bot)
async def aHandler(bot: Client, event: Message):
    print(2)
    async for message in app.get_chat_history(-1001704658427):
        m.append(message)
    if event.chat.id == 948320744:
        slmi(event.id)
        if "don't send" or "processing" or "uploading" or "exhausted" not in event.text:
            if "Title:" or "now" in event.text:
                if len(m) != 0:
                    await app.forward_messages(948320744, -1001704658427, m[0].id)
                    await app.delete_messages(-1001704658427, m[0].id)
                    await sleep(10)
                    m.pop(0)


print("Bot Started !!")
app.run()
