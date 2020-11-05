#Python 多线程爬取豆瓣TOP250
import requests
from bs4 import BeautifulSoup
import threading
import time
import queue
import os
'''
参考 https://blog.csdn.net/mr_blued/article/details/79375905?utm_medium=distribute.pc_relevant.none-task-blog-title-2&spm=1001.2101.3001.4242
'''



#线程1获取网页真实地址并存入队列中 
class geturl(threading.Thread):
    def __init__(self, urlqueue, count, url):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.url = url
        self.count = count
 
     # 线程的运行函数写在run()里面
    def run(self):
        #休息一下==线程2
        time.sleep(5)
        while self.count>=0 and self.count <= 250:
            # 每一页的地址
            page_url = self.url + '?start=' + str(self.count) + '&filter='
            # 将获取的每个地址放入队列中      
            self.urlqueue.put(page_url)
            print('线程1 run put(pageurl) {}'.format(self.count))
            self.urlqueue.task_done()
            # 经抓包分析，每一页都是25部电影的介绍与其他数据
            self.count += 25
            time.sleep(1)



#线程2获取信息并存入TXT文档中
class getcontent(threading.Thread):
    def __init__(self, urlqueue):
                 threading.Thread.__init__(self)
                 self.urlqueue = urlqueue
                 
    def run(self):
            while  True:
                # 基础反爬
                header = {'Referer':'https://www.douban.com/',
                    'User-Agent':
                      'ozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                # 从线程1中的队列里取出存放的地址
                url = self.urlqueue.get()
                # 解析地址，从中获取所需的数据
                res = requests.get(url,headers=header)
                soup = BeautifulSoup(res.text, 'html.parser')
                for contents in soup.select('.info'):
                    if contents.select('.hd') != []:
                        titles = ''.join(contents.select('.hd')[0].text.split())
                        #print(titles)
                    if contents.select('.bd p') != []:   
                        peoples = contents.select('.bd p')[0]
                        name = peoples.contents[0].strip()
                        addrs = peoples.contents[2].strip()
                            #print(name)
                        #print(addrs)
                    score = contents.select('.bd .star .rating_num')[0].text
                    numbers = contents.select('.bd .star span')[3].text#.contents[6]
                    #print (score)
                    #print(numbers)
                    if contents.select('.bd .quote .inq') != []:
                        message = contents.select('.bd .quote .inq')[0].text
                        #print(message)
                    #用列表存取每一部电影的信息
                    content = [titles,name,addrs,
                               score,numbers,message]
                    #创建TXT文档并将列表中的电影信息写入
                    with open('douban.txt','a', encoding='utf-8') as file:
                        for each in content:
                            file.write(each)
                            #空行只是为了美观
                            file.write('\n')
                        file.write('\n')
                        file.write('\n')
                    print('线程2 写入 ')                       
                time.sleep(1)





#线程3检查线程1、2是否运行完毕
class contrl(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue

    def run(self):
        while True:
            print("程序执行中")
            # 该线程休眠 1 分钟，之后检查队列是否为空
            time.sleep(60)
            if (self.urlqueue.empty()):
                print("程序执行完毕！")
                os._exit(0)
     
url = 'https://movie.douban.com/top250'
count = 0
# 创建队列
urlqueue = queue.Queue()
# 线程 1
t1 = geturl(urlqueue, count,url)
t1.start()

# 线程 2
t2 = getcontent(urlqueue)
t2.start()

# 线程 3
t3 = contrl(urlqueue)
t3.start()
