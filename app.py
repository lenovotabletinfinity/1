from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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

    caption_text = f"""<b><blockquote>Hᴇʟʟᴏ {user_first_name}, ᴍʏsᴇʟғ <a href="https://t.me/{bot_username}">{bot_username}</a></blockquote>

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
    
