"""
                                  Alhamdulillah...

So far everything is good, we have managed to create 4 plugins and some other utils.
Everything is fine until you don't message something that is not mentioned in this 
code.

For example:
    if you send some gibberish then, the code will pause. In order for it to start you 
    need to clear the messages mannually and send a "Hi".
"""

from whatsapp.utils.initialize import initialize
from whatsapp.utils.latest_message import latest_message
from whatsapp.utils.messageHandler import messageHandler
from whatsapp.utils.commandHandler import commandHandler


driver, ActionChains, Keys = initialize()


def main():
    try:
        message = latest_message(driver).strip()
    except:
        message = "@#$%^&~!"

    if message[0] == '.':
        commandHandler(driver, message)

    elif message[0] == '@':
        pass

    else:
        messageHandler(driver, message)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print("ERROR:", e)
