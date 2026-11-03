import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = "ТВОЙ_ТОКЕН_БОТА"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

DOWNLOAD_DIR = "./downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Бот запущен и готов к работе! Отправь мне видео.")

@dp.message(lambda message: message.video is not None)
async def handle_video(message: types.Message):
    await message.answer("⏳ Видео получено! (Здесь будет логика загрузки в TikTok).")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
