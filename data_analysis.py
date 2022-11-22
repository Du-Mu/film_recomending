import csv
import json
import matplotlib.pyplot as plt
'''
"bestRating": "10",
        "ratingCount": "70247",
        "ratingValue": "8.6",
        "worstRating": "2"
'''
def analysis_basic_info(csv_file_name):
    header = ['name','data','genre','data','rating_count', 'rating_value']
    csv_file = open(csv_file_name, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(header)

    for i in range(1, 11):
        file = open('./film_data/film'+str(i)+'/basic.json', 'r')
        basic_info = json.load(fp=file)
        row = [
            basic_info['name'],
            basic_info['datePublished'],
            basic_info['genre'],
            basic_info['aggregateRating']['ratingCount'],
            basic_info['aggregateRating']['ratingValue'],
        ]
        writer.writerow(row)
        file.close()
    csv_file.close()


def analysis_addr_info(file_name, film_no):
    file = open(file_name, 'r')
    addr_info = json.load(fp=file)
    file.close()
    
    addr_info['else'] = 0
    for key in list(addr_info.keys()):
        if (addr_info[key] < 8):
            addr_info['else'] += addr_info[key]
            del addr_info[key]

    plt.rcParams['font.sans-serif']=['KaiTi','SimHei','FangSong']
    plt.figure(figsize = (8,8))
    explode = []
    for i in range(0, len(addr_info)):
        explode.append(i*0.01)
    plt.pie(addr_info.values(), labels=addr_info.keys(), explode = explode, autopct = '%1.2f%%',
        pctdistance = 0.8, labeldistance = 0.9)
    plt.title('addr_info')
    plt.savefig('./paper_writing/images/addr'+str(film_no)+'.jpg')

def analysis_rating_info(file_name, film_no):
    file = open(file_name, 'r')
    addr_info = json.load(fp=file)
    file.close()
    
    plt.rcParams['font.sans-serif']=['KaiTi','SimHei','FangSong']
    plt.figure(figsize = (8,8))
    explode = []
    for i in range(0, len(addr_info)):
        explode.append(i*0.01)
    plt.pie(addr_info.values(), labels=addr_info.keys(), explode = explode, autopct = '%1.2f%%',
        pctdistance = 0.8, labeldistance = 0.9)
    plt.title('rating_info')
    plt.savefig('./paper_writing/images/rating'+str(film_no)+'.jpg')


    
