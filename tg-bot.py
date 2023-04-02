import telebot
from telebot import types

bot = telebot.TeleBot("6216567019:AAGbDuRes7Xl5leuTUs_-CCYBak-SXsO1EA")

'''
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привяу")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, я бот-помощник", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Привяу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Новости')
        btn2 = types.KeyboardButton('Расписание')
        btn3 = types.KeyboardButton('Курсы')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    elif message.text == "Какие новости?":
        bot.send_message(message.from_user.id, "Да нормально все, остальные новости по " + "[ссылке](https://levelp.ru/news/)", parse_mode="Markdown")
    elif message.text == "Какое расписание?":
        bot.send_message(message.from_user.id, "Расписание доступно по [ссылке](https://levelp.ru/courses/schedule/)", parse_mode="Markdown")
    elif message.text == "Какие есть курсы?":
        bot.send_message(message.from_user.id, "Список курсов находится по [ссылке](https://levelp.ru/courses/)", parse_mode="Markdown")

bot.polling(none_stop=True, interval=0)


'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я умею /register")
@bot.message_handler(commands=['register'])
def register(message):
    bot.send_message(message.chat.id, "Введите пожалуйста свое имя")
    bot.register_next_step_handler(message, read_name)
def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Введите пожалуйста свою фамилию")
    bot.register_next_step_handler(message, read_sname, name)
def read_sname(message, name):
    sname = message.text
    bot.send_message(message.chat.id, f"Спасибо за регистрацию {name} {sname}")