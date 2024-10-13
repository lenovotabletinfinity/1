import os
from telegram import Update, Sticker
from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
import threading
import time

# Load the bot token from environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Debugging: Check if the token is loaded
if TOKEN:
    print(f"Bot token loaded: {TOKEN[:5]}...")  # Print first five characters for safety
else:
    print("Failed to load TELEGRAM_BOT_TOKEN from environment variables")
    exit(1)  # Exit the program if no token is found

# Initialize the Flask app
app = Flask(__name__)

# Function to handle the /start command
async def start(update: Update, context):
    # React with 🔥
    await update.message.chat.send_action("typing")  # Simulates "reaction" (like 🔥)
    
    # Send sticker
    sticker_id = "CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA"
    sticker_message = await update.message.reply_sticker(sticker_id)
    
    # Wait 2 seconds and delete the sticker
    time.sleep(2)
    await sticker_message.delete()

# Function to run the Telegram bot
def run_telegram_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Add a handler for the /start command
    application.add_handler(CommandHandler("start", start))
    
    # Start the bot
    application.run_polling()

# Start the Flask server
@app.route('/')
def home():
    return "Bot is running!"

# Run the Telegram bot in a separate thread
if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_telegram_bot)
    bot_thread.start()
    
    # Start the Flask app
    app.run(host="0.0.0.0", port=8080)
    
