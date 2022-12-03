import re
import csv
import json
import jieba
import seaborn as sns
from snownlp import SnowNLP
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def analysis_basic_info(csv_file_name):
    header = ['No','name','data','genre','data','rating_count', 'rating_value']
    csv_file = open(csv_file_name, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(header)

    for i in range(1, 11):
        file = open('./film_data/film'+str(i)+'/basic.json', 'r')
        basic_info = json.load(fp=file)
        row = [
            i,
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
    plt.rcParams['font.size']=16
    plt.rcParams['font.style']= 'oblique'
    plt.figure(figsize = (5,5))
    explode = []
    for i in range(0, len(addr_info)):
        explode.append(i*0.01)
    plt.pie(addr_info.values(), labels=addr_info.keys(), explode = explode, autopct = '%2.2f%%',
        pctdistance = 0.8, labeldistance = 1.2)
    plt.title('addr_info')
    plt.savefig('./paper_writing/images/addr'+str(film_no)+'.jpg')
    plt.close()

def analysis_rating_info(file_name, film_no):
    file = open(file_name, 'r')
    addr_info = json.load(fp=file)
    file.close()
    
    plt.rcParams['font.sans-serif']=['KaiTi','SimHei','FangSong']
    plt.rcParams['font.size']=16
    plt.rcParams['font.style']= 'oblique'
    plt.figure(figsize = (5,5))

    explode = []
    for i in range(0, len(addr_info)):
        explode.append(i*0.01)
    plt.pie(addr_info.values(), labels=addr_info.keys(), explode = explode, autopct = '%2.2f%%',
        pctdistance = 0.8, labeldistance = 1.2)
    plt.title('rating_info')
    plt.savefig('./paper_writing/images/rating'+str(film_no)+'.jpg')
    plt.close()

def analysis_comments_info(file_name, film_no): 
    stopwords = [line.strip() for line in open('./stop_word.txt', encoding="utf-8").readlines()]
    pos_word = {}
    neg_word = {}

    file = open(file_name, 'r')
    comments_info = json.load(fp=file)
    file.close()
    com_sentiments = []
    for i in range(1, len(comments_info)+1):
        comment = comments_info[str(i)]['content']
        comment = ' '.join(re.findall('[\u4e00-\u9fa5]+', comment, re.S))
        if comment == '':
            continue
        comment_snow = SnowNLP(comment)
        com_sentiments.append(comment_snow.sentiments)
    sns.distplot(com_sentiments, bins=30)
    plt.rcParams['axes.unicode_minus']=False
    plt.savefig('./paper_writing/images/comments'+str(film_no)+'.jpg')
    plt.close()

    mean = np.mean(com_sentiments)

    for i in range(1, len(comments_info)+1):
        comment = comments_info[str(i)]['content']
        comment = ' '.join(re.findall('[\u4e00-\u9fa5]+', comment, re.S))
        if comment == '':
            continue
        comment_snow = SnowNLP(comment)
        if comment_snow.sentiments > mean:
            now_word = pos_word
        else:
            now_word = neg_word

        words = jieba.lcut(comment)
        for word in words:
            if word in stopwords:
                continue
            if len(word)<2:
                continue
            if now_word.get(word):
                now_word[word]+=1
            else:
                now_word[word] = 1

    keywords_file = open('./paper_writing/keywords/film'+str(film_no)+'.txt','w')
    keywords_file.write("pos_word:\n")
    pos_item = list(pos_word.items())
    pos_item.sort(key=lambda x: x[1], reverse=True)
    for i in range(30):
        p_word, word_count = pos_item[i]
        keywords_file.write(p_word+':'+str(word_count)+',')
    neg_item = list(neg_word.items())
    neg_item.sort(key=lambda x: x[1], reverse=True)
    keywords_file.write("\nneg_word:\n")
    for i in range(30):
        p_word, word_count = neg_item[i]
        keywords_file.write(p_word+':'+str(word_count)+',')
    keywords_file.close()

    return com_sentiments


#analysis_basic_info('./paper_writing/table.csv')

for i in range(1,11):
    analysis_addr_info('./film_data/film'+str(i)+'/addr.json',i)
    analysis_rating_info('./film_data/film'+str(i)+'/rating.json',i)
    analysis_comments_info('./film_data/film'+str(i)+'/comments.json',i)




