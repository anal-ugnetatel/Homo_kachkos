import telebot
from telebot import types
from telebot.types import Message

bot = telebot.TeleBot('6110641577:AAFLP9EcnCD2hH5DS6xTwL8eElNhz3vZeZM')

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton('🦾 Добавить результат')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, " 👋 Поздороваться / \n🦾 Добавить результат", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        img = open('D:\Tg\Homo.PNG', 'rb')
        bot.send_photo(message.from_user.id, img) #ответ бота
        bot.send_message(message.from_user.id, "Привет, Гигус младший, здесь начнется твое становление Сигмой. Okeeey, leets gooo!")

    if message.text == '🦾 Добавить результат':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Жим")
        btn2 = types.KeyboardButton("Подтягивания")
        btn3 = types.KeyboardButton("Становая")
        btn4 = types.KeyboardButton("Присед")
        btn5 = types.KeyboardButton("/start")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5)
        bot.send_message(message.from_user.id, "Покажи всем на что ты способен)", reply_markup=markup)

    if message.text == 'Жим':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        name_sport = message.text
        btn1 = types.KeyboardButton("Добавить результат")
        btn2 = types.KeyboardButton("Изменить результат")
        btn3 = types.KeyboardButton("/start")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.from_user.id,"Ты уже вносил достижения?", reply_markup=markup)
        bot.register_next_step_handler(message, get_result, name_sport)




    if message.text == 'Присед':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        name_sport = message.text
        btn1 = types.KeyboardButton("Добавить результат")
        btn2 = types.KeyboardButton("Изменить результат")
        btn3 = types.KeyboardButton("/start")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.from_user.id,"Ты уже вносил достижения?", reply_markup=markup)
        bot.register_next_step_handler(message, get_result, name_sport)



    if message.text == 'Становая':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        name_sport = message.text
        btn1 = types.KeyboardButton("Добавить результат")
        btn2 = types.KeyboardButton("Изменить результат")
        btn3 = types.KeyboardButton("/start")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.from_user.id,"Ты уже вносил достижения?", reply_markup=markup)
        bot.register_next_step_handler(message, get_result, name_sport)



    if message.text == 'Подтягивания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        name_sport = message.text
        btn1 = types.KeyboardButton("Добавить результат")
        btn2 = types.KeyboardButton("Изменить результат")
        btn3 = types.KeyboardButton("/start")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.from_user.id,"Ты уже вносил достижения?", reply_markup=markup)
        bot.register_next_step_handler(message, get_result, name_sport)


def get_result(message, name_sport):
    if message.text == "Добавить результат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Введи свой результат в кг в дисцеплине " + name_sport, reply_markup=markup)




bot.polling(none_stop=True)


