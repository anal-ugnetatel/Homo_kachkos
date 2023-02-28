import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6110641577:AAFLP9EcnCD2hH5DS6xTwL8eElNhz3vZeZM')

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()



def db_table_val(user_id: int, user_name: str, press:int, pull_up:int, sit:int, stan:0):
    cursor.execute('INSERT INTO users (user_id, user_name, press, pull_up, sit, stan) VALUES (?, ?, ?,?, ?, ?)', (user_id, user_name, press,pull_up, sit, stan))
    conn.commit()
def update_InfoInBd(message):
    print(message)
    print("Подключен к SQLite")
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    true = 0
    id = 0
    for row in records:
        if int(row[1]) == int(message.from_user.id):
            true = 1
            id = row[0]
    if true == 1:
        sql_update_query = """Update users set user_id =""" + str(message.from_user.id) + """ where id =""" + str(id)
        cursor.execute(sql_update_query)
        conn.commit()
        print("Запись успешно обновлена")

    else:
        us_id = message.from_user.id
        us_name = message.from_user.first_name

        db_table_val(user_id=us_id, user_name=us_name, press=0, pull_up=0, sit=0, stan=0 )
        print("Запись успешно добавлена")

def update_press(message, name_sport):
    print(message)
    print("Подключен к SQLite")
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    true = 0
    id = 0
    for row in records:
        if row[1] == message.from_user.id:
            id = row[0]
    if name_sport== "Подтягивания":
        name_sport = "pull_up"
    if name_sport== "Жим":
        name_sport = "press"
    if name_sport== "Присед":
        name_sport = "sit"
    if name_sport== "Становая":
        name_sport = "stan"
    sql_update_query = """Update users set """+name_sport+""" =""" + message.text + """ where id =""" + str(id)
    cursor.execute(sql_update_query)
    conn.commit()
    print("Запись успешно обновлена "+name_sport)

def rating_up(message, name_sport):
    print("Подключен к SQLite")
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    if message.text == "Жим":
        bot.send_message(message.from_user.id, "Рейтинг по Жиму:")
        for row in records:
            print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            bot.send_message(message.from_user.id, row[2] + " = " + str(row[3]))

    if message.text == "Присед":
        bot.send_message(message.from_user.id, "Рейтинг по Приседу:")
        for row in records:
            bot.send_message(message.from_user.id, row[2] + " = " + str(row[5]))
    if message.text == "Становая":
        bot.send_message(message.from_user.id, "Рейтинг по Становой:")
        for row in records:
            bot.send_message(message.from_user.id, row[2] + " = " + str(row[6]))
    if message.text == "Подтягивания":
        bot.send_message(message.from_user.id, "Рейтинг по Подтягиваниям:")
        for row in records:
            bot.send_message(message.from_user.id, row[2]+" = "+str(row[4]))




@bot.message_handler(commands=['start'])
def start(message):
    update_InfoInBd(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton('🦾 Добавить результат')
    btn3 = types.KeyboardButton('Рейтинг🌏')
    markup.add(btn1, btn2)
    markup.add(btn3)
    bot.send_message(message.from_user.id, " 👋 Поздороваться / \n🦾 Добавить результат/\n🌏 Смотреть Рейтинг",
                     reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        img = open('D:\Tg\Homo.PNG', 'rb')
        update_InfoInBd(message)
        bot.send_photo(message.from_user.id, img)  # ответ бота
        bot.send_message(message.from_user.id,
                         "Привет, Гигус младший, здесь начнется твое становление Сигмой. Okeeey, leets gooo!")
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
    update_press(message, name_sport)
    bot.send_message(message.from_user.id, "Ваш результат: " + message.text + " кг", reply_markup=markup)
    bot.register_next_step_handler(message, rating)


def add_result(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    name_sport = message.text
    btn1 = types.KeyboardButton("/start")
    markup.add(btn1)
    bot.send_message(message.from_user.id, name_sport + ":\nВведи свой максимальный результат в КГ: ",
                     reply_markup=markup)
    bot.register_next_step_handler(message, get_result, name_sport)


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
        bot.send_message(message.from_user.id,
                         "Абсолютный pound for pound рейтинг:\n вася пупки 400 кг\n Антон флеер 700кг ",
                         reply_markup=markup)
        bot.send_message(message.from_user.id, "Можешь выбрать свое коронное движение, чтобы увидеть лучших в нем!: ")
        bot.register_next_step_handler(message, rating)
    if message.text == 'Жим':
        rating_up(message, "press")
    if message.text == 'Присед':
        rating_up(message, "sit")
    if message.text == 'Становая':
        rating_up(message, "stan")
    if message.text == 'Подтягивания':
        rating_up(message, "pull_up")
    if message.text == '/start':
        start(message)


bot.polling(none_stop=True)
