import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading

# Load the bot's token from an environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # React to the /start command
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker='CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA')

    # Schedule sticker deletion
    threading.Timer(2, delete_sticker, [update.effective_chat.id, context]).start()

async def delete_sticker(chat_id, context):
    # Wait for the message to be sent before attempting to delete it
    await context.bot.delete_message(chat_id=chat_id)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler('start', start))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
                                       
