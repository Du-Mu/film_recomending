import os
import time
import requests
import json
from bs4 import BeautifulSoup

headers = {
    'Accept':'*/*',
    'Cookie':'bid=2elG84guidY; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14248; __yadk_uid=RfKuYZYDKXa9dAKYOvIAOqJoOdrkkOX9; ll="108304"; __utmz=30149280.1668852797.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="142488132:Gw/TAzRNLC8"; ck=lJdk; __utmc=30149280; __utma=30149280.1243899161.1666871492.1668938684.1668942243.7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1668942263%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utmb=30149280.2.10.1668942243; _pk_id.100001.8cb4=b09ce958df6258eb.1666871490.6.1668943331.1668940085.; ap_v=0,6.0',
    'DNT':'1',
    'Host':'movie.douban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

'''
{
    'film':film-name',
    1:
        'id':''
        'content':''
        'add':''
    },
    2:{
        ...
    }
}
[film struct]
'''


def film_reviews_spider(film_link, film_info, rating_data, addr_data):
    start_num = 0;
    count = 0
    while (start_num < 1000):
        print('[*]now are loading '+str(start_num)+' comments')
        start_num += 100
        review_url = film_link+'comments?start='+str(start_num)+'&limit=100&status=P&sort=new_score'
        time.sleep(5)
        try:
            review_html = requests.get(url=review_url, headers=headers).text
        except Exception:
            print('[*]fail to parse:'+review_url)
            return False
        review_soup = BeautifulSoup(review_html, 'html.parser')

        for i in review_soup.find_all('div', 'comment'):
            count += 1

            addr = i.find('span', 'comment-location').text
            rating = i.contents[1].contents[3].contents[5].get('title')

            comment_info = {
                'id':i.contents[1].contents[3].contents[1].text,
                'content':i.find('span', 'short').text,
                'addr':addr,
                'rating':rating
            }

            if (rating_data.get(rating) == None and len(rating) == 2):
                rating_data[rating] = 1
            elif (len(rating) == 2):
                rating_data[rating] += 1
            
            if (addr_data.get(addr) == None):
                addr_data[addr] = 1
            else:
                addr_data[addr] += 1
                
            film_info[str(count)] = comment_info

    return True

def get_basic_data(film_url):
    time.sleep(1)
    film_main_html = requests.get(url=film_url, headers=headers).text
    
    film_main_soup = BeautifulSoup(film_main_html, 'html.parser')

    basic_info = film_main_soup.find('script', type='application/ld+json').text
    
    return json.loads(basic_info, strict = False)


def get_film_id():
    film_url = 'https://movie.douban.com/chart'
    film_html = requests.get(url=film_url, headers=headers).text
    film_soup = BeautifulSoup(film_html, 'html.parser')
    num = 0

    for i in film_soup.find_all('a', 'nbg'):
        rating_data = {}
        addr_data = {}
        basic_data = {}
        num+=1

        print('[-]now are processing film ' + str(num))

        film_name = i.get('title')
        film_info = {'title':film_name}
        film_reviews_spider(film_link=i.get('href'), film_info=film_info, rating_data=rating_data, addr_data=addr_data)
        basic_data = get_basic_data(i.get('href'))

        try:
            os.mkdir('./film_data/film'+str(num))
        except Exception:
            continue

        file = open('./film_data/film'+str(num)+'/comments.json', 'w')
        json.dump(film_info, fp=file, sort_keys=True, separators=(',', ': '), indent=4, ensure_ascii=False)
        file.close()

        file_addr = open('./film_data/film'+str(num)+'/addr.json', 'w')
        json.dump(addr_data, fp=file_addr, sort_keys=True, separators=(',', ': '), indent=4, ensure_ascii=False)
        file_addr.close()

        file_rating = open('./film_data/film'+str(num)+'/rating.json', 'w')
        json.dump(rating_data, fp=file_rating, sort_keys=True, separators=(',', ': '), indent=4, ensure_ascii=False)
        file_rating.close()

        file_basic = open('./film_data/film'+str(num)+'/basic.json', 'w')
        json.dump(basic_data, fp=file_basic, sort_keys=True, separators=(',', ': '), indent=4, ensure_ascii=False)
        file_basic.close()
    
get_film_id()