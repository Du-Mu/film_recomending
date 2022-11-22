import json
import requests
from bs4 import BeautifulSoup


headers = {
    'Accept':'*/*',
    'Cookie':'bid=2elG84guidY; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14248; __yadk_uid=RfKuYZYDKXa9dAKYOvIAOqJoOdrkkOX9; ll="108304"; __utmz=30149280.1668852797.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="142488132:Gw/TAzRNLC8"; ck=lJdk; __utmc=30149280; __utma=30149280.1243899161.1666871492.1668938684.1668942243.7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1668942263%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utmb=30149280.2.10.1668942243; _pk_id.100001.8cb4=b09ce958df6258eb.1666871490.6.1668943331.1668940085.; ap_v=0,6.0',
    'DNT':'1',
    'Host':'movie.douban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}
headers = {
    'Accept':'*/*',
    'Cookie':'bid=2elG84guidY; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14248; __yadk_uid=RfKuYZYDKXa9dAKYOvIAOqJoOdrkkOX9; ll="108304"; __utmz=30149280.1668852797.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="142488132:Gw/TAzRNLC8"; ck=lJdk; __utmc=30149280; __utma=30149280.1243899161.1666871492.1668938684.1668942243.7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1668942263%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utmb=30149280.2.10.1668942243; _pk_id.100001.8cb4=b09ce958df6258eb.1666871490.6.1668943331.1668940085.; ap_v=0,6.0',
    'DNT':'1',
    'Host':'movie.douban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}
url = 'https://movie.douban.com/subject/3042261/'

r = requests.get(url=url, headers=headers).text

r = BeautifulSoup(r, 'html.parser')



def kkk(film):
    film =json.loads(r.find('script', type = 'application/ld+json').text)
    
film = {}
kkk(film)

print(film)