from telegram import Update, Sticker
from telegram.ext import Updater, CommandHandler, CallbackContext
import time
import threading

# Your bot's token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    # React to the /start command
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker='CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA')

    # Schedule sticker deletion
    threading.Timer(2, delete_sticker, [update.effective_chat.id, context]).start()

def delete_sticker(chat_id, context):
    context.bot.delete_message(chat_id=chat_id)

def main() -> None:
    updater = Updater(TOKEN)

    # Register the /start command handler
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
