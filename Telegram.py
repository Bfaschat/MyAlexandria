import telebot
import TelegramToken
import Parsing
import time

bot = telebot.TeleBot(TelegramToken.Token)

users = []
count = 0

f = open('Users.txt')
count = int(f.readline())
users = []
for i in range(count):
    users.append(int(f.readline()))
f.close()

@bot.message_handler(content_types=['text'])
def handler_text(user):
    global users
    global count

    message = user.text
    print(time.ctime(time.time()),'Message from', user.from_user.first_name, user.from_user.last_name, message)

    if message == 'Krasava':
        bot.send_message(user.chat.id,'<pre>==My respect to you==</pre>',parse_mode='HTML')

    if message == '/last':
        Posts = Parsing.parse('https://myalexandriya.blogspot.com/', 0, 0)
        for New_Post in Posts:
            bot.send_message(user.chat.id,"<b>" + New_Post['title'] + "</b>" + chr(10) + chr(10) + New_Post['text'] + chr(10) + chr(10) + "<a href = \"" + New_Post['url'] + "\">Читать полностью...</a>",parse_mode='HTML')

    if message == '/status':
        bot.send_message(user.chat.id,'Server is running')

    Vrubaem = True
    if message == 'Нет':
        Vrubaem = False

    if message == 'Выдать последние 5':
        Posts = Parsing.parse('https://myalexandriya.blogspot.com/', 0, 4)
        for New_Post in Posts:
            bot.send_message(user.chat.id,"<b>" + New_Post['title'] + "</b>" + chr(10) + chr(10) + New_Post['text'] + chr(10) + chr(10) + "<a href = \"" + New_Post['url'] + "\">Читать полностью...</a>", parse_mode = 'HTML')

    if message == 'Выдать последние 10':
        Posts = Parsing.parse('https://myalexandriya.blogspot.com/', 0, 9)
        for New_Post in Posts:
            bot.send_message(user.chat.id,"<b>" + New_Post['title'] + "</b>" + chr(10) + chr(10) + New_Post['text'] + chr(10) + chr(10) + "<a href = \"" + New_Post['url'] + "\">Читать полностью...</a>", parse_mode='HTML')

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
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Выдать последние 5', 'Выдать последние 10')
        user_markup.row('Не надо')
        bot.send_message(user.chat.id, 'Выдать последние новости?',reply_markup=user_markup)

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

while True:
    try:
        bot.polling(none_stop=False, interval=0)
        print('lol')
    except Exception as e:
        for i in range(15):
            print('')
