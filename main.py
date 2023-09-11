import asyncio
from dotenv import load_dotenv
from os import getenv, listdir
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random

load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    # await message.reply("Привет")
    await message.answer("Привет")

@dp.message(Command("photo"))
async def send_random_picture(message: types.Message):
    images_folder = "images/"
    images = [f for f in listdir(images_folder) if f.endswith(("856.jpg", "1556705578_2.jpg", "Z5ized368Gg.jpg"))]
    if images:
        random_image = random.choice(images)
        file = types.FSInputFile(images_folder + random_image)
        await message.answer_photo(file)
    else:
        await message.answer("В папке с картинками нет подходящих файлов.")


@dp.message(Command("myinfo"))
async def my_info(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    info_message = f"Ваш ID: {user_id}\nИмя: {first_name}\nUsername: @{username}"
    await message.answer(info_message)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())