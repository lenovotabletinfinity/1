import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.executor import start_webhook

# Load environment variables (API_ID, API_HASH, TOKEN, WEBHOOK_URL)
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
    # React with typing action
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

    # Caption text for the image
    caption_text = f"""<b><blockquote>Hᴇʟʟᴏ {user_first_name}, ᴍʏsᴇʟғ <a href="https://t.me/{bot_username}">{bot_username}</a></blockquote></b>

Wᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ? I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀɴʏ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ."""

    # Inline buttons
    keyboard = InlineKeyboardMarkup()
    button_anime_channel = InlineKeyboardButton(text="✭ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ ✭", url="https://t.me/Cartoon_Carnival")
    button_about_me = InlineKeyboardButton(text="❀ Aʙᴏᴜᴛ Mᴇ ❀", callback_data="about_me")
    keyboard.add(button_anime_channel)
    keyboard.add(button_about_me)

    # Send the image with the caption and buttons
    image_url = "https://files.catbox.moe/w34293.jpg"
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption=caption_text,
        parse_mode="HTML",
        reply_markup=keyboard  # Attach inline buttons
    )


# Callback handler for the "❀ Aʙᴏᴜᴛ Mᴇ ❀" button
@dp.callback_query_handler(lambda callback_query: callback_query.data == "about_me")
async def show_about_me(callback_query: types.CallbackQuery):
    try:
        # First loading animation step
        loading_step_1 = "▣☐☐"
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=loading_step_1
        )
        await bot.answer_callback_query(callback_query.id)  # Acknowledge the callback

        # Wait for 1 second
        await asyncio.sleep(1)

        # Second loading animation step
        loading_step_2 = "☐▣☐"
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=loading_step_2
        )

        # Wait for 1 second
        await asyncio.sleep(1)

        # Third loading animation step
        loading_step_3 = "☐☐▣"
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=loading_step_3
        )

        # Wait for 1 second before showing the final about me text
        await asyncio.sleep(1)

        # Final About Me details with "🔙 Bᴀᴄᴋ" button
        bot_username = (await bot.me).username
        about_me_caption = f"""<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
        
‣ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/{bot_username}">{bot_username}</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ  : <a href='https://t.me/Nobita_MUI'>Nᴏʙɪᴛᴀ</a>
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://render.com'>Rᴇɴᴅᴇʀ</a>
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""

        # Add the "🔙 Bᴀᴄᴋ" button
        keyboard = InlineKeyboardMarkup()
        back_button = InlineKeyboardButton(text="🔙 Bᴀᴄᴋ", callback_data="back_to_start")
        keyboard.add(back_button)

        # Update the caption with the final about me details and the "🔙 Bᴀᴄᴋ" button
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=about_me_caption,
            parse_mode="HTML",
            reply_markup=keyboard  # Attach the back button
        )

    except Exception as e:
        print(f"Error handling about_me callback: {e}")
        # Optionally, send a message if something went wrong
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Sorry, something went wrong while handling your request."
        )


# Callback handler for the "🔙 Bᴀᴄᴋ" button
@dp.callback_query_handler(lambda callback_query: callback_query.data == "back_to_start")
async def back_to_start(callback_query: types.CallbackQuery):
    try:
        # First loading animation step
        loading_step_1 = "▣☐☐"
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=loading_step_1
        )
        await bot.answer_callback_query(callback_query.id)

        # Wait for 1 second
        await asyncio.sleep(1)

        # Second loading animation step
        loading_step_2 = "☐▣☐"
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=loading_step_2
        )

        # Wait for 1 second
        await asyncio.sleep(1)

        # Third loading animation step
        loading_step_3 = "☐☐▣"
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption=loading_step_3
        )

        # Wait for 1 second before going back to the start message
        await asyncio.sleep(1)

        # Call the start command to resend the initial message
        message = callback_query.message  # Get the message to pass to the start command
        await start_command(message)  # Correctly call the start command

    except Exception as e:
        print(f"Error handling back_to_start callback: {e}")
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Sorry, something went wrong while handling your request."
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
            host="0.0.0.0",  # Bind to 0.0.0.0 for Render
            port=PORT,       # Use the port from the environment
        )
    else:
        from aiogram import executor
        executor.start_polling(dp, skip_updates=True)
    
