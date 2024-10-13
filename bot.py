import os
import time
import logging
from flask import Flask
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, CommandHandler
import threading

# Enable logging to track events
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize Flask for port binding
app = Flask(__name__)

# Flask route to keep Render happy by binding to port
@app.route('/')
def index():
    return "Bot is running!"

# Telegram bot functionality
TOKEN = os.getenv('')  # Read token from environment variable

async def start(update: Update, context):
    logger.info("Received /start command")  # Log the command reception

    # React with 🔥 by simulating a typing action for 2 seconds
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    time.sleep(2)  # Simulate typing time to represent the "reaction"

    # Send the sticker
    sticker_message = await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker='CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA')
    
    # Wait for 2 seconds
    time.sleep(2)

    # Delete the sticker
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=sticker_message.message_id)
    logger.info("Sticker sent and deleted successfully")  # Log sticker sent and deleted

async def error_handler(update, context):
    logger.error(f'Update {update} caused error {context.error}')  # Log errors

def run_telegram_bot():
    # Initialize the bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Add /start handler
    app.add_handler(CommandHandler("start", start))

    # Set up the error handler
    app.add_error_handler(error_handler)

    # Start polling for Telegram updates
    logger.info("Starting the bot in polling mode")
    app.run_polling()

if __name__ == '__main__':
    # Run Telegram bot in a separate thread
    bot_thread = threading.Thread(target=run_telegram_bot)
    bot_thread.start()

    # Get the port from the environment variable, default to 8080
    port = int(os.getenv('PORT', 8080))

    # Start Flask app on the specified port
    app.run(host='0.0.0.0', port=port)
    
