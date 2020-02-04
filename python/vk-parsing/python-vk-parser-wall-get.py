###Данный скрипт позволяет получить список url для загрузки с пабликов/личных страничек
###Первый вариант - метод wall.get

from urllib import request
import requests
import csv

outputfile = "list of girls url.txt"

numberofurl = 20000




def take_1000_posts():
    token = 'eb02be31eb02be31eb02be3188eb6d3f64eeb02eb02be31b53bd02ede0a22dab11283a7'
    version = 5.103
    domain = 'worldbeautifulwoman'
    #domain = 'lanin'
    count = 100
    offset = 0
    all_posts = []

    while offset < numberofurl:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_photo(data):
    file = open(outputfile, 'w')
    for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            print(img_url)
            file.write(img_url + '\n')

    file.close()

all_posts = take_1000_posts()
file_photo(all_posts)

