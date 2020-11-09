# -*- codeing = utf-8 -*-
#@author : Sai
import requests
from bs4 import BeautifulSoup 
import os
import sys
import time
import random 
import webbrowser
import pandas
import lxml
#多线程
import threading
import queue

# try:
url = 'https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8/49823770'
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
req = requests.get(url, headers=headers)
bs = BeautifulSoup(req.content, 'lxml')

pandas.set_option('display.max_rows', None)
#每列中文对齐
pandas.set_option('display.unicode.ambiguous_as_wide', True)
pandas.set_option('display.unicode.east_asian_width', True)
pandas.set_option('max_colwidth',100)
#数据超过总宽度后，是否折叠显示
pandas.set_option('expand_frame_repr', False)
#生成dataframe对象
df = pandas.read_html('url', attrs={"log-set-param" : "table_view"})
print(df)
#删除最后一项是参考资料 NaN
df.pop(len(df)-1)

th = ['集数', '标题', '原创', '登场']
flag = 0
for each in df:
    #py3使用.fillna替换NaN为0
    each.fillna(value=0, inplace=True)
    #第二项1 单独处理
    flag += 1 #标记第二项
    if flag == 2:
        each.columns = ['']*len(each.columns)
        #删除年份和标题（集数 标题……）
        each.drop([0, 1], inplace=True)
        continue
    #删除年份
    each.drop(0, inplace=True)
    each = each.loc[: , th]
        #写入文件
    # with open('test.txt','a+',encoding='utf-8') as f:
    #     f.write(str(each) + '\n')

# except Exception as identifier:
#     print('这是错误 ',identifier)





















# #Test 源码
# try:
#     url = 
#     headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
#     req = requests.get(url, headers=headers)
#     bs = BeautifulSoup(req.text, 'lxml')
    
#     #4个列表
#     hd_list = bs.select('.info .hd')
#     bd_list = bs.select('.info .bd')
#     rate_list = bs.select('.rating_num')
#     quote_list = bs.findAll('p',class_='quote')
#     for i in range(25):
#         with open("豆瓣电影爬虫第一页.txt","a+", encoding='utf-8') as f:
#             f.write("".join(hd_list[i].a.text.split()) + '\t' + \
#                 rate_list[i].text+ '\n\t' + \
#                 "".join(bd_list[i].p.text.split('\n')[1].strip() + \
#                     bd_list[i].p.text.split('\n')[2].strip()) + '\n\t' + \
#                 quote_list[i].span.text +'\n')
# except Exception as err:
# 	print('这是错误', err)



# url = 'https://search.bilibili.com/'
# search = input('搜索的内容：')
# webbrowser.open(url + 'all?keyword=' + search)

# url='https://gary666.com/learn?page=1'
# rep = requests.get(url)
# rep.encoding = rep.apparent_encoding
# # print(rep.text)
# soup = BeautifulSoup(rep.content, 'html.parser') #解析器 ？lxml
# page_list = soup.find_all('div', class_='blogs')
# # print(page_list)
# f = open('bs4标题Test.txt', 'w+')
# for i in page_list:
# 	f.write('文章名:' + i.find('h3').string + '\n'*2)
# f.close()