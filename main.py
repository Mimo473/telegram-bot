import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "PUT_YOUR_TOKEN_HERE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("أهلاً فيك 👋\nالبوت شغال 24/7 🚀")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("الأوامر:\n/start\n/help")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())