import os
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

from function import predict

TOKEN = os.environ['TOKEN']

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Класс состояний
class Newsstage(StatesGroup):
    news = State()
    nextones = State()


# Обработка команды start
@dp.message_handler(commands=["start"])
async def process_start_comand(message: types.Message):
    user = message.from_user.first_name
    await bot.send_message(message.from_user.id, f"Привет {user}!!\nДавай начнем угадывать!!\nНапиши 'Да'")


# Обработка команды help
@dp.message_handler(commands=["help"])
async def process_help_comand(message: types.Message):
    user = message.from_user.first_name
    print(message.from_user.id)
    await bot.send_message(message.from_user.id, f"{user}, напиши мне 'Да', и я попоробую угадать тему твоей новости!")

# Получение сообщений от пользователя
@dp.message_handler()
async def get_text_message(message: types.Message):
    text = message.text
    user = message.from_user.first_name
    if text.lower().replace(" ", "") == "да":
        question = f"""Привет {user}, я могу угадать тематику текста. Я умею различать такие темы:Россия, Мир, Экономика, Спорт, Культура, Наука и техника, Интернет и СМИ, Бывший СССР, Из жизни, Дом, Силовые структуры, Украина, Ценности, Бизнес, Путешествия. Хочешь попробовать?"""
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        await bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, f"{user}, я тебя не понимаю напиши '/help'")


# Обработка повторного использования бота
@dp.message_handler(state=Newsstage.news)
async def predict_news(message: types.Message, state: FSMContext):
    text = message.text
    user = message.from_user.first_name
    await bot.send_message(message.from_user.id, f"{user}, я думаю тематика твоей новости: '{predict(text)}'")
    await Newsstage.next()
    question = f"Хочешь попробовать еще раз?"
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    await bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


# Обработка нажатия клавиш
@dp.callback_query_handler(lambda c: c.data, state="*")
async def callback_worker(callback_query: types.CallbackQuery):
    if callback_query.data == "yes":
        await bot.send_message(callback_query.from_user.id,
                               f"""Пожалуйста скопируй и вставь любую новость с новостного сайта""")
        await Newsstage.news.set()
    elif callback_query.data == "no":
        await bot.send_message(callback_query.from_user.id, f"Напиши мне 'да', если передумаешь")


if __name__ == "__main__":
    executor.start_polling(dp)
