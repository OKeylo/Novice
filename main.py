from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from currency.currency_command import currency_command
from aiogram.types import InputMediaPhoto
from wallpaper.parser import image_parser


bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!\nИспользуй /help, чтобы узнать список доступных команд!')

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = 'Я могу ответить на следующие команды:\n /photo\n /arguments\n /currency  /curr\n /wallpaper'
    await message.answer(msg)
#TODO: parsing is not a preview of the photo, but real ones and add an error handler
@dp.message_handler(commands=['wallpaper'])
async def process_wallpaper_command(message: types.Message):
    images = image_parser(message.text) 
    media = [InputMediaPhoto(image) for image in images]
    await bot.send_media_group(message.from_user.id, media)

@dp.message_handler(commands=['arguments'])
async def test(message: types.Message):
    msg = [ msg for msg in message.text.split(" ")][1::]
    await message.answer(msg)

@dp.message_handler(commands=['currency', 'curr'])
async def process_currency_command(message: types.Message):
    msg = currency_command(message.text)
    await message.answer(msg)

if __name__ == '__main__':
    executor.start_polling(dp)
    