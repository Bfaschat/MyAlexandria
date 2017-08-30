import urllib.request
from bs4 import BeautifulSoup

def parse(url,index):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(),'html.parser')
    table = soup

    allpost = []

    for row in table.find_all(class_='post-outer'):
        post = row.find_all(class_='post hentry')
        title = post[0].find_all(class_='post-title entry-title')
        text = post[0].find_all(class_='post-body entry-content')
        posturl = post[0].find_all(class_='post-title entry-title')
        image = post[0].find_all('table')

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
            'imageurl': image[0].a.get('href')
        })

    return(allpost[index])