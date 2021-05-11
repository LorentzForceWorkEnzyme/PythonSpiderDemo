import os
import json
import requests
import re
import time

# from collections import OrderedDict
# import xlrd 
# import pandas as pd
# import openpyxl
# import operator

domain = []
full_name = []
id = []
followers_count = []
location = []
skills = []
software = []
headline = []
hearders = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
proxies={
    #'https':'127.0.0.1:'
}

myid = ''

try: 
    s = requests.Session()
    s.keep_alive = False
   
    
    ##20个画师1个page，50page就是1000个画师
    for i in range(1,50):
        url='https://www.artstation.com/users/'+ myid+'/following.json?page=' + str(i)
        res = requests.get(url=url, headers=hearders, proxies=proxies, timeout=10)

        #遇到最后一页，中止请求
        if len(res.text)<100:
            print('最后一页关注画师，中止!',i, res.status_code)
            break
        s = res.json()
        
        # 写入50个page文件
        os.makedirs('JSON', exist_ok=True)
        with  open(os.path.join('JSON/ArtstationPage-'+str(i)+'.json'), 'w+') as items:
            json.dump(s, items, sort_keys=True,  indent=4)
        print(len(res.text),'正常写入Page-')

    #写入ArtstationPage文件
    for i in range(1,43):
        with open(os.path.join('JSON/followingPage/ArtstationPage-'+str(i)+'.json'), 'r') as items:
            #data_json是一个list有20个dict,'id, subdomain/suername, followers_count, full_name
            data_json = json.load(items)['data']
            
            for j in range(len(data_json)):
                domain.append((data_json[j]['subdomain']))
                full_name.append(data_json[j]['full_name'])
                id.append(data_json[j]['id'])
                followers_count.append(data_json[j]['followers_count'])
                location.append(data_json[j]['location'])
                skills.append([i['name'] for i in data_json[j]['skills']])
                software.append([i['name'] for i in data_json[j]['software_items']])
                headline.append(re.split('[^(\w | @ | \. | \|)]+', data_json[j]['headline']))
             
    artists_json = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "data":[
            {}
        ]
    }
    for i in range(len(id)):
        temp_json = {
            "id":id[i],
            "full_name":full_name[i],
            "subdomain_and_username":domain[i],
            "headline":headline[i],
            "url":"https://www.artstation.com/" + domain[i],
            "location":location[i],
            "skills":skills[i],
            "software":software[i],
            "followers_count":followers_count[i],
        }
        artists_json['data'].append(temp_json)
    print(len(artists_json['data']))

    # 写入
    os.makedirs('JSON', exist_ok=True)
    with  open(os.path.join('JSON/ArtstationArtists.json'), 'w+') as items:
        json.dump(artists_json, items, indent=4, )
    print('正常写入')

except Exception as e:
    print(e)