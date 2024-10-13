import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
import os
import time
from flask import Flask
from telegram import Update
from telegram.constants import ChatAction  # Use the updated import path
from telegram.ext import ApplicationBuilder, CommandHandler
import threading

# Initialize Flask for port binding
app = Flask(__name__)

# Flask route to keep Render happy by binding to port
@app.route('/')
def index():
    return "Bot is running!"

# Telegram bot functionality
TOKEN = '7714661974:AAE5jUkm9M9deeBTzsABuo0JkPMJpjVxnA4'

async def start(update: Update, context):
    # React with 🔥 by simulating a typing action for 2 seconds
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    time.sleep(2)  # Simulate typing time to represent the "reaction"

    # Send the sticker
    sticker_message = await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker='CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA')
    
    # Wait for 2 seconds
    time.sleep(2)

    # Delete the sticker
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=sticker_message.message_id)

async def error_handler(update, context):
    print(f'Update {update} caused error {context.error}')

def run_telegram_bot():
    # Initialize the bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Add /start handler
    app.add_handler(CommandHandler("start", start))

    # Start polling for Telegram updates
    app.run_polling()

if __name__ == '__main__':
    # Run Telegram bot in a separate thread
    bot_thread = threading.Thread(target=run_telegram_bot)
    bot_thread.start()

    # Get the port from the environment variable, default to 8080
    port = int(os.getenv('PORT', 8080))

    # Start Flask app on the specified port
    app.run(host='0.0.0.0', port=port)
    
