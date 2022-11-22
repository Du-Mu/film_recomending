# file_recomending 
 
Crawler for film critics from douban.com  
  
# Basic Framework  

- using crawler get data about film from douban.com  
    - get_data.py  
    - get a json file including films data, short commonts and commontator's ip address
- NLP for analyzing  
    - analyze_data.py

data file struct:  

```bash
film_recomending
--|--film_data
  |  |--film1_data
  |  |  |--addr.json
  |  |  |--basic.json
  |  |  |--comments.json
  |  |  |--rating.json
  |  |--film2_data
  |  ...
  |--paper_writing
  |  |--Film-Analysis-Based-on-NLP.tex
  |  |--images/
  |--get_data.py
  |--data_analysis.py
```

## dependence
- requests
  处理web交互

- bs4
  html处理

- matplotlib
  画图处理

- snowNLP
  NLP


# Paper Planning

## Abstract
## Modul
## Data Analysis
  - 影片基本信息
    - 表格化处理
  - 地区分布
    - 画出扇形分布图
  - 评论处理
    - 对于每一个评论做一个分词处理:提取关键词
    - 对于每一个评论做情感分析:细化分数
    - 对分析做一个正态函数拟合:获取均值
    - 统计情感分数分词频度:获取高频关键词
## Related Work
snowNLP

## Evaluation
对于情感分析和分数做一个准确度分析
判断偏差值