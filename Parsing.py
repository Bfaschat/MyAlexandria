import urllib.request
from bs4 import BeautifulSoup
import time

def parse(url,index1, index2):
    allpost = []
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response.read(),'html.parser')
        table = soup

        row = table.find_all(class_='post-outer')
        for i in range(index2-index1+1):
            k = i+index1
            post = row[k].find_all(class_='post hentry')
            title = post[0].find_all(class_='post-title entry-title')
            text = post[0].find_all(class_='post-body entry-content')
            posturl = post[0].find_all(class_='post-title entry-title')

            text = text[0].div.text

            title = title[0].a.text

            title = title.replace(u'\xa0',u' ')
            text = text.replace(u'\xa0',u' ')

            for i in range(len(text)):
                if text[i] == chr(10) and i > 0:
                    break

            allpost.append({
                'title': title,
                'text': text[1:i],
                'url': posturl[0].a.get('href'),
            })
    except Exception as e:
        print('Error ',e)
        return('Error')

    print(time.ctime(time.time()), 'all nice')
    return(allpost)