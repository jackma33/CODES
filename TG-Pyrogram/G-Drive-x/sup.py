from naabo import Config
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

app = Client("my_account",
             api_id=15918522,
             api_hash="689382b9f19dbc03d0dd12ce157438dc",
             session_string=Config.stringSession)


@app.on_message(filters.bot)
def handle_message(bot:Client, event:Message):
    bot.send_message(948320744, "/start")
    a = bot.get_messages(948320744, 36742)
    print(a)


print("!!!")
app.run()
