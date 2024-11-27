from aiogram import Dispatcher, types
async def start_command(message: types.Message):
    await message.reply("Привет! Я помогу тебе отправить домашнее задание. Введи команду /homework, чтобы начать.")

def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])