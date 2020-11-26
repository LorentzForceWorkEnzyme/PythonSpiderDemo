# -*- coding: utf-8 -*-
# @Author:xiaozhu_sai
# @title: B站自动登录
# Status: 未完成
#Date: 2020/11/24

#参考:https://github.com/wkunzhi/Python3-Spider
#   https://blog.csdn.net/hhy1107786871/article/details/88342976

"""
验证码大图目前无法文字识别,即无法继续后续位置、鼠标点击等操作实现
    例：图：https://static.geetest.com/nerualpic/word_l1_zh_2020.11.13/harley1/318697e5b844c0e979406c5a8e3b25ca.jpg?challenge=57d957f83a22778465c7190d899c47c2
提交后，验证后，增加“手机短信验证码”环节
本脚未继续操作，即只实现————输入信息，点击登录，（识别上图文字）
"""
import time
import base64
import random
import os

#导入baidu_aip
from aip import AipOcr
from PIL import Image

import webbrowser
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# #配置chromedriver.exe在chrome和python路径
# CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'


class bilibiliLogin:

    loginURL = 'https://passport.bilibili.com/login'
    _account = 'xxx'
    _password = 'xxx'
    
    #初始化
    def __init__(self): 
        
        #定义浏览器
        self._brower = webdriver.Chrome()
        #显式等待，直到找到某个元素.
        self.wait = WebDriverWait(self._brower, 20)

        #阻止报错
        '''
        ERROR:device_event_log_impl.cc(211)] [13:42:04.043] 
        USB: usb_device_handle_win.cc:1020 
        Failed to read descriptor from node connection:
         连到系统上的设备没有发挥作用。 (0x1F)
        '''
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level = 3')

    #输入信息, 点击登录
    def browerInput(self):

        # 账号输入框输入
        self.wait.until(
            ec.presence_of_element_located((By.ID, 'login-username'))
            ).send_keys(self._account)
        # self._brower.find_element_by_id('login-username').send_keys(self._account).clear()

        #密码输入框输入
        self.wait.until(
            ec.presence_of_element_located((By.ID, 'login-passwd'))
        ).send_keys(self._password)
        # self._brower.find_element_by_id('login-passwd').send_keys(self._password)

        #获取登录按钮
        self.wait.until(
            ec.presence_of_element_located((By.CLASS_NAME, 'btn-login'))
        ).click()
        # btn = self._brower.find_element(By.CLASS_NAME, 'btn-login').click()
        time.sleep(5)

    #验证码识别
    def captcha(self):
        self.imgDownload()
        self.imgSplit()
        self.imgChangeLight()
        #未完成 < img1 >
        self.captcha()

    #下载验证图片
    def imgDownload(self):
        #等待加载验证图片
        self.wait.until(
            ec.presence_of_element_located((By.CLASS_NAME, 'geetest_item_img'))
        )
        _imgSrc = self._brower.find_element_by_class_name('geetest_item_img').get_attribute('src')
        # print(_imgSrc)

        #照片写入文件
        f = open(file = 'image.jpeg',mode = 'wb')
        for i in requests.get(_imgSrc).iter_content(100000):
            f.write(i)
        f.close()
        
    #图片切割
    def imgSplit(self):
        img = Image.open('image.jpeg')
        #切割，上图img1，下图img2
        img.crop((0,0,344,342)).save('img1.jpeg')
        img.crop((0, 342, 120, 384)).save('img2.jpeg')
                
    #图片二值化
    def imgChangeLight(self):
        im = Image.open('img1.jpeg')
        # n可理解为色阶的灰调数值
        im1 = im.point(lambda p: p * 1).save("new_img1.jpeg")

    #图片文字识别
    def imgReco(self):
        '''
        调用“百度智能云 通用文字识别（含位置）”
        50次/每天
        https://ai.baidu.com/tech/imagecensoring
        '''
        # # 打开图片img2
        # with open('img2.jpeg', 'rb') as f:
        #   gf = f.read()

        #ID KEY SECRETKEY
        WAPPID = 'xxx'
        WAPPKEY = 'xxx'
        WSECRETKEY = 'xxx'
        op = {'language_type': 'CHN_ENG', 'recognize_granularity': 'small'}
        #使用百度云智能 
        WCLIENT = AipOcr(WAPPID, WAPPKEY, WSECRETKEY)
        
        ## 返回word为字典。['words_result']为识别结果
        word = WCLIENT.accurate(gf, options=op)
        imgSrt = word['words_result']

        return imgSrt



    #开始，登录入口
    def login(self):
        # 打开浏览器
        self._brower.get(self.loginURL)
        # 账号和密码，点击登录
        self.browerInput()

        #验证码 
        #img1无法识别，暂时搁置
        # self.captcha()


try:
    if __name__ == "__main__":
        L = bilibiliLogin()

        L.login()
      
except Exception as error:
    print('错误 ',error)


