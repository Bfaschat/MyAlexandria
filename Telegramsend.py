import telebot
import TelegramToken
import Parsing
import time

bot = telebot.TeleBot(TelegramToken.Token)

index1 = 0
index2 = 0

Last_Post = Parsing.parse('https://myalexandriya.blogspot.com/', index1, index2)

while True:
    New_Post = Parsing.parse('https://myalexandriya.blogspot.com/',index1, index2)
    if Last_Post != New_Post:
        f = open('Users.txt')
        count = int(f.readline())
        users = []
        for i in range(count):
            users.append(int(f.readline()))
        f.close()
        if New_Post != 'Error':
            for i in range(count):
                print('Sending to',users[i])
                bot.send_message(users[i], "<pre>========New Post========</pre>" + chr(10) + "<b>" + New_Post[0]['title'] + "</b>" + chr(10) + chr(10)  + New_Post[0]['text'] + chr(10) + chr(10)  + "<a href = \""+New_Post[0]['url']+"\">Читать полностью...</a>",parse_mode='HTML')
            Last_Post = New_Post

    time.sleep(25)