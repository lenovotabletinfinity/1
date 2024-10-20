from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler
import os

# Define the bot token
TOKEN = os.getenv("TOKEN")  # Load the token from environment variables

async def start(update: Update, context):
    """Handler for /start command. Add a 🔥 reaction to the user's message."""
    # Add a reaction to the user's message
    await context.bot.send_reaction(
        chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
        emoji="🔥"
    )

if __name__ == "__main__":
    # Create the bot application
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handler for the /start command
    start_handler = CommandHandler("start", start)
    app.add_handler(start_handler)

    # Start polling to listen for incoming messages
    app.run_polling()
    
