import imp


import sys
import glob
import importlib


plugins = []
filesPathList = glob.glob('.\\whatsapp\\plugins\\*.py')
for plugin in filesPathList:
    plugin = plugin.split('\\')[-1].split('.')[0]
    plugins.append(plugin)


def commandHandler(driver, message):
    cmd = message.replace('.', '').split(' ')[0]
    if cmd in plugins:
        module = importlib.import_module(f'whatsapp.plugins.{cmd}')
        plugin = getattr(module, cmd)
        reply = plugin(driver, cmd)
        if reply == 'STOP':
            sys.exit()
