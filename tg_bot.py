from aiogram import Bot, Dispatcher, types, F
from config import token
from aiogram.filters.command import Command
import asyncio
from main import get_10_new_article
import keyboards
#logging.basicConfig(level=logging.INFO)5

bot = Bot(token=token)
dp = Dispatcher()
#, parse_mode="HTML"

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}.Пожалуйста, введи число, сколько новостей ты хочешь получить")

@dp.message(F.text())
async def count_article(message: types.Message):
    user_input=message.text
    a = int(user_input)
    await message.answer(f"Хорошо, вы увидите первые {a} популярных новостей за последнее время" ,reply_markup = keyboards.main_kb)

#@dp.message(F.text.lower() == "показать новости")
@dp.message()
async def echo(message: types.Message):
    msg = message.text.lower()
    if msg == "показать новости":
        for el in get_10_new_article(a):
            await bot.send_message(message.from_user.id,el, reply_markup=keyboards.news_kb,)
    elif msg == "выбор новостей":
        await message.answer("Какие новости вы ходите видеть?", reply_markup=keyboards.filter_kb())
    elif msg == "назад":
        await message.answer("Вы перешли в главное меню!", reply_markup=keyboards.main_kb)


@dp.message(F.text=="показать новости")
async def get_articles(message:types.Message):
    for el in get_10_new_article():
        await bot.send_message(message.from_user.id,el)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
