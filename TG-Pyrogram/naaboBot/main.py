from naabo import Config
from naabo.utils.mongo import BotDataBase
from naabo.utils.message_handler import MessageHandler
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

import glob
import importlib

plugins = []
filesPathList = glob.glob('.\\naabo\\plugins\\*.py')
for plugin in filesPathList:
    plugin = plugin.split('\\')[-1].split('.')[0]
    plugins.append(plugin)


db = BotDataBase()
app = Client("my_account",
             api_id=15918522,
             api_hash="689382b9f19dbc03d0dd12ce157438dc",
             session_string=Config.stringSession)


@app.on_message(filters.command(plugins, prefixes=['.']) & filters.me)
async def commandHandler(bot: Client, event: Message):
    cmd = event.text.replace('.', '').split(' ')[0]
    # await event.edit(text=cmd)
    if cmd in plugins:
        module = importlib.import_module(f'naabo.plugins.{cmd}')
        plugin = getattr(module, cmd)
        await plugin(bot, event)


@app.on_message(filters.private & ~filters.bot)
async def privateMessageHandler(bot: Client, event: Message):
    if db.checkIfBlackListed(event.chat.id) == True and event.outgoing == False:
        await bot.delete_messages(chat_id=event.chat.id, message_ids=event.id)

    elif db.checkIfWhiteListed(event.chat.id) == False:
        MessageHandler(bot, event)


@app.on_message(filters.group)
async def groupMessageHandler(bot: Client, event: Message):
    # print(event.text)
    pass


print("Bot Started !!")
app.run()
