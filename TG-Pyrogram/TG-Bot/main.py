import glob
import importlib
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from bot.MessageHandler import MessageHandler


app = Client("bot")


plugins = []
filesPathList = glob.glob('.\\bot\\plugins\\*.py')
for plugin in filesPathList:
    plugin = plugin.split('\\')[-1].split('.')[0]
    plugins.append(plugin)


@app.on_message(filters.command(plugins, prefixes=['/']) & filters.private)
async def commandHandler(bot: Client, event: Message):
    cmd = event.text.replace('/', '').split(' ')[0]
    if cmd in plugins:
        module = importlib.import_module(f'bot.plugins.{cmd}')
        plugin = getattr(module, cmd)
        await plugin(bot, event)


@app.on_message(filters.group)
async def groupMessageHandler(bot: Client, event: Message):
    if event.from_user.id == 976223233:
        print("OWNER's Message")
    else:
        print("other's Message")
        await MessageHandler(bot, event)


print("Bot Started !!")
app.run()
