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

bot.polling(none_stop=True, interval=3)