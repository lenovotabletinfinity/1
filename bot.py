import time
from telegram import Update, Sticker
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = '7714661974:AAE5jUkm9M9deeBTzsABuo0JkPMJpjVxnA4'

async def start(update: Update, context):
    # React with 🔥
    await update.message.reply_chat_action('typing')  # Using 'typing' action to simulate a reaction

    # Send the sticker
    sticker_message = await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker='CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA')
    
    # Wait for 2 seconds
    time.sleep(2)

    # Delete the sticker
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=sticker_message.message_id)

async def error_handler(update, context):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
                
