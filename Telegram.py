import telebot
import TelegramToken

bot = telebot.TeleBot(TelegramToken.Token)

users = []
count = 0

@bot.message_handler(content_types=['text'])
def handler_text(user):
    global users
    global count

    message = user.text
    print('Message from', user.from_user.first_name, user.from_user.last_name, message)

    Vrubaem = True
    if message == '/stop' or message == 'Нет':
        Vrubaem = False

    if message == '/start' or message == 'Да':
        boolean = True
        for i in range(count):
            if users[i] == user.chat.id:
                boolean = False
        if boolean == True:
            count += 1
            users.append(user.chat.id)
            f = open('Users.txt','w')
            f.writelines("%s\n" % count)
            f.writelines("%s\n" % i for i in users)
            f.close()
            print('New User:', user.from_user.first_name, user.from_user.last_name, user.chat.id)
        bot.send_message(user.chat.id,'Сейчас функция отправки новостей включена. Вы можете отключить её в любой момент: /stop')

    if message == '/stop':
        if user.chat.id in users:
            count -= 1
            users.remove(user.chat.id)
            f = open('Users.txt', 'w')
            f.writelines("%s\n" % count)
            f.writelines("%s\n" % i for i in users)
            f.close()
            print('User Left:', user.from_user.first_name, user.from_user.last_name, user.chat.id)

    if message == '/help':
        bot.send_message(user.chat.id,'/start - Начать присылать новости')
        bot.send_message(user.chat.id,'/stop - Прекратить пересылать новости')

    if user.chat.id not in users and Vrubaem:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Да','Нет')
        bot.send_message(user.chat.id,'У вас не включена функция отправки новостей, включить?',reply_markup=user_markup)


bot.polling(none_stop=True, interval=3)