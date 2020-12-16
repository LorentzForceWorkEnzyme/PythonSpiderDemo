import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
import time
import os

user = 'xxx'
password = 'xxx'
url = 'http://10.255.255.222/a70.htm'

#设置浏览器参数
options = webdriver.ChromeOptions()
options.add_argument('--log-level = 3')
#     ## 打开端口测试 chrome.exe --remote-debugging-port=51228 --user-data-dir="C:\selenum\AutomationProfile"
# options.add_experimental_option("debuggerAddress", "127.0.0.1:51228")

#创建浏览器
_browser = webdriver.Chrome(
    options=options
)
#打开网页
_browser.get(url)
bWait = WebDriverWait(_browser, 4, 0.2)


#输入信息，点击登录
def login():
    _browser.find_element_by_name('f3').find_element_by_name('DDDDD').send_keys(user)
    _browser.find_element_by_name('f3').find_element_by_name('upass').send_keys(password)
    Select(_browser.find_element_by_name('ISP_select')).select_by_index(1)

    button1 = _browser.find_element_by_css_selector('input[value^="登"]')
    _browser.execute_script("arguments[0].click();",button1)

#是否已登录，已登录返回True
def isLoginSucceed():
    '''
    判断“注销“按钮，name=‘logout’唯一值
    '''
    try:
        _browser.find_element_by_name('logout')
        return True
    except:
        return False

#判断是否需要重新登录，需要返回True
def isOther():
    '''
    判断是否出现id=’message'，唯一
    '''
    try:
        _browser.find_element_by_id('message')
        return True  
    except:
        #登录成功
        return False

#确认网络
def isNet():
    res = requests.get('http://www.baidu.com')
    if str(res).find('200') > -1:
        return False
    else:
        return True

def main():
    while not isLoginSucceed():
        #第一次登录
        login()

        #已登录
        if isLoginSucceed():
            _browser.execute_script('alert("isLoginSucceed已经登录，1秒后关闭")')
            time.sleep(1)
            _browser.switch_to.alert.accept()
            _browser.quit()
            break

        #未登录成功
        if isOther() and isNet():
            time.sleep(1)
            #检测到message，，点击“返回”
            button1 = _browser.find_element_by_name('GobackButton')
            _browser.execute_script("arguments[0].click();",button1)
            continue
    
            
      
if __name__ == '__main__':
    main()
    print('ending')