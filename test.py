import requests
from bs4 import BeautifulSoup
'''
headers=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
'Cookie':'bid=2elG84guidY; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14248; __yadk_uid=RfKuYZYDKXa9dAKYOvIAOqJoOdrkkOX9; ll="108304"; __utmz=30149280.16688527护是另一回事。（可能这是豆瓣关闭API的主要原因之一）。但是可以引入诸如社区管理，甚至是收费。我们不能因为某个原因就选择“简单粗暴”的解决方法。正是因为难，一件事才有了更大的意义。

刚刚看了《监视资本主义：智能陷阱 The Social Dilemma 》这部纪录片，片中除了普及了关于社交网络的种种问题，也在试图唤醒我们使用互联网的初衷，以及这些年来一直忽视的互联网的人本主义。一直以来我们都把人的注意力当成了“商品”，不断地去攫取这种资源。而不是将人性放到更重要的角度的审视。97.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="142488132:Gw/TAzRNLC8"; ck=lJdk; __utmc=30149280; __utma=30149280.1243899161.1666871492.1668938684.1668942243.7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1668942263%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utmb=30149280.2.10.1668942243; _pk_id.100001.8cb4=b09ce958df6258eb.1666871490.6.1668943331.1668940085.; ap_v=0,6.0'
},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
'''

headers = {
    'Accept':'*/*',
    'Cookie':'bid=2elG84guidY; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14248; __yadk_uid=RfKuYZYDKXa9dAKYOvIAOqJoOdrkkOX9; ll="108304"; __utmz=30149280.1668852797.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="142488132:Gw/TAzRNLC8"; ck=lJdk; __utmc=30149280; __utma=30149280.1243899161.1666871492.1668938684.1668942243.7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1668942263%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utmb=30149280.2.10.1668942243; _pk_id.100001.8cb4=b09ce958df6258eb.1666871490.6.1668943331.1668940085.; ap_v=0,6.0',
    'DNT':'1',
    'Host':'movie.douban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}
url = 'https://movie.douban.com/subject/3042261/comments?status=P'

r = requests.get(url=url, headers=headers).text

r = BeautifulSoup(r, 'html.parser')

k = r.find_all('div', 'comment')
#print(r.content)
for i in k:
    print(i.contents[1].contents[3].contents[5].get('title'))

