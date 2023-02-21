import telebot
from telebot import types

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
bot.polling(none_stop=True)


