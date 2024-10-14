import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.executor import start_webhook

# Load environment variables
API_ID = os.getenv("API_ID")          # API ID from environment
API_HASH = os.getenv("API_HASH")      # API Hash from environment
API_TOKEN = os.getenv("TOKEN")        # Bot token from environment
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Webhook URL from environment
PORT = int(os.getenv("PORT", 8080))   # Default port 8080

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Webhook settings
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL_FULL = f"{WEBHOOK_URL}{WEBHOOK_PATH}"

# Webhook mode or polling mode
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "True").lower() == "true"

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # React with typing action (this will simulate an interaction)
    await bot.send_chat_action(message.chat.id, action="typing")

    # Send the sticker
    sticker_id = 'CAACAgUAAxkBAAIg0mcLMMWYOB-RqDzBRsGYmg4nDLtTAAIEAAPBJDExieUdbguzyBAeBA'
    sent_sticker = await message.answer_sticker(sticker_id)

    # Wait for 2 seconds before deleting the sticker
    await asyncio.sleep(2)
    await bot.delete_message(chat_id=message.chat.id, message_id=sent_sticker.message_id)

    # Send the image with the caption
    user_first_name = message.from_user.first_name  # Get the user's first name
    bot_username = (await bot.me).username          # Get the bot's username

    caption_text = f"""<b><blockquote>Hᴇʟʟᴏ {user_first_name}, ᴍʏsᴇʟғ <a href="https://t.me/{bot_username}">{bot_username}</a></blockquote></b>

Wᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ? I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀɴʏ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ."""
   

    # Inline button
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="✭ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ ✭", url="https://t.me/Cartoon_Carnival")
    keyboard.add(button)

    # Send the image with the caption and the button
    image_url = "https://files.catbox.moe/w34293.jpg"
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption=caption_text,
        parse_mode="HTML",  # To enable HTML formatting in the caption
        reply_markup=keyboard  # Attach the inline button
    )

# Startup and shutdown actions
async def on_startup(dp):
    if USE_WEBHOOK:
        await bot.set_webhook(WEBHOOK_URL_FULL)
    else:
        await bot.delete_webhook()

async def on_shutdown(dp):
    if USE_WEBHOOK:
        await bot.delete_webhook()
    await bot.close()

# Main entry point for webhook or polling
if __name__ == '__main__':
    if USE_WEBHOOK:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host="0.0.0.0",  # Render binds to 0.0.0.0
            port=PORT,  # Explicitly bind to port 8080
        )
    else:
        from aiogram import executor
        executor.start_polling(dp, skip_updates=True)
