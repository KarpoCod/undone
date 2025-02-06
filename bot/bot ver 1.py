import telebot

#1982738900:AAEfJAYKUXkEs8IJjRA7lCn26F7FzXLh5K8

bot = telebot.TeleBot('1982738900:AAEfJAYKUXkEs8IJjRA7lCn26F7FzXLh5K8')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '-_-')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'привет жалкий человечишка')
    elif message.text == 'Пока':
        bot.reply_to(message, 'досвидания уважаемый')
    bot.reply_to(message, message.text)

bot.polling()
