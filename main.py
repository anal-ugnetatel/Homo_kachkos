import telebot
from telebot import types


bot = telebot.TeleBot('6110641577:AAFLP9EcnCD2hH5DS6xTwL8eElNhz3vZeZM')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton('🦾 Добавить результат')
    btn3 = types.KeyboardButton('Рейтинг🌏')
    markup.add(btn1, btn2)
    markup.add(btn3)
    bot.send_message(message.from_user.id, " 👋 Поздороваться / \n🦾 Добавить результат/\n🌏 Смотреть Рейтинг", reply_markup=markup)
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
        bot.send_message(message.from_user.id, "Покажи всем на что ты способен в: ", reply_markup=markup)

    if message.text == 'Жим':
        add_result(message)
    if message.text == 'Присед':
            add_result(message)
    if message.text == 'Становая':
        add_result(message)
    if message.text == 'Подтягивания':
        add_result(message)
    if message.text == 'Рейтинг🌏':
        rating(message)



def get_result(message, name_sport):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Рейтинг🌏')
    btn2 = types.KeyboardButton("/start")
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.from_user.id, "Ваш результат: "+message.text+" кг",reply_markup=markup )
    bot.register_next_step_handler(message, rating)


def add_result(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    name_sport = message.text
    btn1 = types.KeyboardButton("/start")
    markup.add(btn1)
    bot.send_message(message.from_user.id, name_sport+ ":\nВведи свой максимальный результат в КГ: " , reply_markup=markup)
    bot.register_next_step_handler(message, get_result,name_sport)

def rating(message):
    if message.text == 'Рейтинг🌏':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Жим")
        btn2 = types.KeyboardButton("Подтягивания")
        btn3 = types.KeyboardButton("Становая")
        btn4 = types.KeyboardButton("Присед")
        btn5 = types.KeyboardButton("/start")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5)
        bot.send_message(message.from_user.id, "Абсолютный pound for pound рейтинг:\n вася пупки 400 кг\n Антон флеер 700кг ", reply_markup=markup)
        bot.send_message(message.from_user.id, "Можешь выбрать свое коронное движение, чтобы увидеть лучших в нем!: ")
        bot.register_next_step_handler(message, rating)
    if message.text == 'Жим':
        bot.send_message(message.from_user.id, "Рейтинг по Жиму:")
        bot.register_next_step_handler(message, rating)
    if message.text == 'Присед':
        bot.send_message(message.from_user.id, "Рейтинг по Присяду:")
        bot.register_next_step_handler(message, rating)
    if message.text == 'Становая':
        bot.send_message(message.from_user.id, "Рейтинг по Становой:")
        bot.register_next_step_handler(message, rating)
    if message.text == 'Подтягивания':
        bot.send_message(message.from_user.id, "Рейтинг по Подтягиваниям:")
        bot.register_next_step_handler(message, rating)
    if message.text == '/start':
        start(message)









bot.polling(none_stop=True)


