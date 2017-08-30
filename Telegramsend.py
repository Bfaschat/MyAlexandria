import telebot
import TelegramToken
import Parsing
import time
import urllib.request as urllib2

bot = telebot.TeleBot(TelegramToken.Token)

Last_Post = []

k = 0
while True:
    New_Post = Parsing.parse('https://myalexandriya.blogspot.com/',k)
    k += 1
    if Last_Post != New_Post:
        f = open('Users.txt')
        count = int(f.readline())
        users = []
        for i in range(count):
            users.append(int(f.readline()))
        f.close()
        print(New_Post['title'])
        print('------------')
        for i in range(count):
            url = New_Post['imageurl']
            urllib2.urlretrieve(url, 'MyAlexandriaImage.jpg')
            #img = open('MyAlexandriaImage.jpg', 'rb')
            bot.send_message(users[i], "======New Post======" + chr(10) + "<b>" + New_Post['title'] + "</b>" + chr(10) + chr(10)  + New_Post['text'] + chr(10) + chr(10)  + "<a href = \""+New_Post['url']+"\">Читать полностью...</a>",parse_mode='HTML')
            #bot.send_photo(users[i], img)
            #img.close()
    time.sleep(5)

    Last_Post = New_Post