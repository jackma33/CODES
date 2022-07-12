from pyperclip import copy
from telegram.ext import *

API_KEY = "1887448307:AAEsFpRga9Ih1Zo2XAbO4HuSx9t6POB6uN8"
updater = Updater(API_KEY)

def start_command(update, context):
    update.message.reply_text('This Bot was Made By Team NAABO.')

def handle_message(update, context):
    text = str(update.message.text)
    if text == 'NAABO':
        update.message.reply_text(input("Type your message here: "))
        print("Sent :)")
    else:
        print(text+'\n')
        copy(text)
        update.message.reply_text("Sent :)")

def main():
    updater = Updater(API_KEY,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()

    print('Bot Started...\n')
    updater.idle()

main()
