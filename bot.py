import logging

from aiogram import Bot, Dispatcher, executor, types
from search_wiki import get_wiki_page

API_TOKEN = '5816510725:AAEEwqNVQ8B5luHZMLm6iwEvvz_oThKvh4E'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton("Admin bilan bog`lanish")
)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom men Wiki", reply_markup=menu)


# text, video, document, photo, animation, sticker, voice, audio
@dp.message_handler(content_types=['text'])
async def user_text_handler(message: types.Message):
    user_text = message.text
    result = get_wiki_page(user_text)
    if result:
        await message.answer(result)
    else:
        await message.answer("🙃 Malumot topilmadi❗️")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)