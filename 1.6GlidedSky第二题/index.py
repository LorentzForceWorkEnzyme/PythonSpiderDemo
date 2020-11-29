# GlidedSky 第二题
# @Author: xiaozhu_sai
# Date: 2020/11/26
"""
这里有一个网站，还是求所有数字的和，只是这次分了1000页。
待爬取网站 http://www.glidedsky.com/level/web/crawler-basic-2

步骤：
    打开 http://www.glidedsky.com/login
    登录
    打开题目2页面
    爬取数据，求总, 提交
"""
import time
import requests
from bs4 import BeautifulSoup
import threading

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class GlidedShy:
    
    #初始化浏览器
    def __init__(self):

        options = webdriver.ChromeOptions()
        #屏蔽显示 
        #   ERROR:device_event_log_impl.cc
        options.add_argument('--log-level = 3')
        #接管浏览器
        #   chrome.exe --remote-debugging-port=57305 --user-data-dir="C:\selenum\AutomationProfile"
        options.add_experimental_option("debuggerAddress", "127.0.0.1:57305")
    
        #创建浏览器，打开登录网站
        _loginURL = 'http://www.glidedsky.com/login'
        self._brower = webdriver.Chrome(options=options)
        self._brower.get(_loginURL)
    
    #自动登录
    def login(self):
        #验证登录
        if  EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')):
            #弹窗1s后关闭
            self._brower.execute_script("alert('已登录')")
            time.sleep(1)
            self._brower.switch_to.alert.accept()
            return 0
            
        #self.email = 'test@qq.com'
        #self.email = 'x'
        self.email= input("请输入你的QQ邮箱的QQ(不必填写@qq.com)\n")  + '@qq.com'
        self.password  = input("请输入密码，注意遮挡\n")

        # 等待输入框出现
        WebDriverWait(self._brower, 10).until(
            EC.presence_of_all_elements_located((By.ID, 'email'))
        )
        
        self._brower.find_element_by_id('email').send_keys(self.email )
        self._brower.find_element_by_id('password').send_keys(self.password)
        self._brower.find_element_by_class_name('btn-primary').click()

        #点击登录，等待1s
        time.sleep(1)
        #密码/邮箱输入错误
        if EC.text_to_be_present_in_element('class', 'invalid-feedback')  :
            errorBrower = self._brower.find_element_by_xpath(
                '//*[@id="app"]/main/div[1]/div/div/div/div[2]/form/div[1]/div/span/strong'
            )
            print(errorBrower.text)
            self.email = input("请重新输入你的QQ邮箱的QQ(不必填写@qq.com)\n")
            self.password = input("请重新输入密码，注意遮挡\n")
            self.login()
        
    #进入题目网页
    def clickQuestion(self, n):
        #等待网络
        time.sleep(1)

        #获取题目URL list，第0个元素是title
        a = self._brower.find_elements_by_class_name('d-flex')
        QN = a[n]
        
        #已通过————Passed
        if QN.find_element_by_tag_name('span').text == 'Passed':
            self.passedShow()
        else:
            # #浏览器切换到题目页面
            self._brower.get(QN.find_element_by_tag_name('a').get_attribute('href'))
        
    # 题目1
    def Q1(self):
        '''
        方法1(使用)
        直接bs4计算数据界面的数据，无需跳转两次界面

        方法2(未使用)
        点击链接，跳转到数字界面，求和，然后跳转回题目界面.
        优点：方便调试和人机交互
        缺点：需要管理/反复跳转多个句柄
            #获得当前网页句柄——网页标签
            n = self._brower.window_handles
            #切换当前标签
            self._brower.switch_to.window(n[-1])
            #点击"待爬取网站"
            self._brower.find_element_by_xpath('//*[@id="app"]/main/div[1]/div/div/div/div/a').click()
            self._brower.find_element_by_class_name('row').text
            #切换到题目标签
            self._brower.switch_to.window(n[-2])
        '''

        #判断/进入题目1页面
        self.clickQuestion(1)
        
        #获取数据
        self._brower.get('http://www.glidedsky.com/level/web/crawler-basic-1')
        bs = BeautifulSoup(self._brower.page_source, 'html.parser')
        nums_list = bs.select('.card-body .row .col-md-1')

        #计算求和
        sum = 0
        for item in nums_list:
            sum += int(item.text.strip())
        print(sum)

        #提交答案
        self._brower.find_element_by_name('answer').send_keys(sum)
        self._brower.find_element_by_tag_name('button').click()

    #题目2
    def Q2 (self):

        #判断/进入题目2页面
        self.clickQuestion(2)
        
        #开始时间
        a = time.time()

        sum = 0
        for i in range(1, 1001):
            self._brower.get('http://www.glidedsky.com/level/web/crawler-basic-2?page=' + str(i))
            bs = BeautifulSoup(self._brower.page_source, 'html.parser')
            nums_pageList = bs.select('.row .col-md-1')
            for item in nums_pageList:
                sum += int(item.text.strip())

        #结束时间
        b = time.time()
        print(b-a)
        
        #提交答案
        self._brower.find_element_by_name('answer').send_keys(sum)
        self._brower.find_element_by_tag_name('button').click()


    #已通过
    def passedShow(self):
        #Console Test
        print(self._brower.title,' Passed')
        #弹窗
        self._brower.execute_script("alert('已通过')")
        time.sleep(1)
        self._brower.switch_to.alert.accept()
        #返回题目主页
        self._brower.get('http://www.glidedsky.com/')
        
if __name__ == "__main__":

    #打开官网，制作driver
    G1 = GlidedShy()
    # #自动登录,已登录会跳过
    # G1.login()

    # # #题目1 
    # G1.Q1()

    # ## 题目2 
    G1.Q2()


