# -*- codeing = utf-8 -*-
#@author : Sai
import requests
import os
import sys
from bs4 import BeautifulSoup 
import random 

# url = 'https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8/49823770'
url='https://gary666.com/learn?page=1'
rep = requests.get(url)
rep.encoding = rep.apparent_encoding
# print(rep.text)

soup = BeautifulSoup(rep.content, 'html.parser') #解析器 ？lxml
page_list = soup.find_all('div', class_='blogs')
# print(page_list)

f = open('bs4标题Test.txt', 'w+')
for i in page_list:
	f.write('文章名:' + i.find('h3').string + '\n'*2)
f.close()

