import telebot
import TelegramToken
import Parsing
import time

bot = telebot.TeleBot(TelegramToken.Token)

Last_Post = []

index = 0

while True:
    New_Post = Parsing.parse('https://myalexandriya.blogspot.com/',index)
    index += 1
    if Last_Post != New_Post:
        f = open('Users.txt')
        count = int(f.readline())
        users = []
        for i in range(count):
            users.append(int(f.readline()))
        f.close()
        for i in range(count):
            bot.send_message(users[i], "<pre>======New Post======</pre>" + chr(10) + "<b>" + New_Post['title'] + "</b>" + chr(10) + chr(10)  + New_Post['text'] + chr(10) + chr(10)  + "<a href = \""+New_Post['url']+"\">Читать полностью...</a>",parse_mode='HTML')
    time.sleep(5)
    Last_Post = New_Post