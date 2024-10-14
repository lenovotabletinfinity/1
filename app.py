import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook

# Load environment variables (API_ID, API_HASH, TOKEN, WEBHOOK_URL)
API_ID = os.getenv("API_ID")         # API ID from environment
API_HASH = os.getenv("API_HASH")     # API Hash from environment
API_TOKEN = os.getenv("TOKEN")       # Bot token from environment
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Webhook URL from environment
PORT = int(os.getenv("PORT", 8080))  # Default port 8080

# Webhook settings
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL_FULL = f"{WEBHOOK_URL}{WEBHOOK_PATH}"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Webhook settings (True if using webhook, False if polling)
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "True").lower() == "true"

# Reaction to "/start" command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # React with 🔥 (interaction, not a message)
    await bot.send_chat_action(message.chat.id, action="typing")

    # Send the sticker
    sticker_id = 'CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA'
    sent_sticker = await message.answer_sticker(sticker_id)

    # Wait for 2 seconds
    await asyncio.sleep(2)

    # Delete the sticker
    await bot.delete_message(chat_id=message.chat.id, message_id=sent_sticker.message_id)


async def on_startup(dp):
    if USE_WEBHOOK:
        await bot.set_webhook(WEBHOOK_URL_FULL)
    else:
        await bot.delete_webhook()


async def on_shutdown(dp):
    if USE_WEBHOOK:
        await bot.delete_webhook()
    await bot.close()


if __name__ == '__main__':
    if USE_WEBHOOK:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host="0.0.0.0",
            port=PORT,
        )
    else:
        from aiogram import executor
        executor.start_polling(dp, skip_updates=True)
