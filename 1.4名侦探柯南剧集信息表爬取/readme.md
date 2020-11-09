https://blog.csdn.net/weixin_42375356/article/details/109584272
（on csdn）

## 爬虫练习 2
 爬取百度百科“名侦探柯南各集列表”网页
目标：
> https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8/49823770
> 
 ### 爬取数据的目的以及后续处理：
 目的：清楚每一集的登场人物，方便追番（bushi），老二次元了（比如fbi kid 酒厂等）
 1. [ x ] 获取名侦探柯南剧集数据/表格
 2. [  ]  将“登场”数据添加在Bilibili名侦探柯南TV的每一集剧集标题
 3. [  ]  由于剧集集数对应在国内有多个版本，可能会使用查找算法将其标题对齐操作.by jquery?js? 
   
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201109202516660.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM3NTM1Ng==,size_16,color_FFFFFF,t_70#pic_center)

   
*使用框架：request bs4 pandas以及基本frame*
```python
#codeing = utf-8
#@author: xiaozhu_Sai
import requests
from bs4 import BeautifulSoup 
import os
import sys
import time
import random 
import webbrowser
import pandas
   url = 'https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8/49823770'
   headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
   req = requests.get(url, headers=headers)
   bs = BeautifulSoup(req.content, 'html.parser')
       ##测试建议使用下载的静态网页，血的教训
   # bs = BeautifulSoup('名侦探柯南各集列表_百度百科.html', 'html.parser')

   pandas.set_option('display.max_rows', None)
   #每列中文对齐
   pandas.set_option('display.unicode.ambiguous_as_wide', True)
   pandas.set_option('display.unicode.east_asian_width', True)
   pandas.set_option('max_colwidth',100)
   #数据超过总宽度后，是否折叠显示
   pandas.set_option('expand_frame_repr', False)
   #生成dataframe对象
   df = pandas.read_html(url, attrs={"log-set-param" : "table_view"})
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
       with open('优化的表格.txt','a+',encoding='utf-8') as f:
           f.write(str(each) + '\n')
	       ##测试
	       #print(str(each))
```

- 首先是制作requests对象，使用header伪装成浏览器，制作bs对象三部曲。
- pandas.set_option的设置主要是解决爬取的dataframe会省略中间的大部分数据、中文导致对齐问题。参考*https://blog.csdn.net/weekdawn/article/details/81389865*
- 其他都比较正常，网页表格方面有两个需要注意的地方。
	- 变量flag的引入是为了标记表格第二个元素，也不知道什么原因，第二项即“1997年 43-85集”的cloumns、0行、1行和其他12行都不一样，只能单独使用flag+判断语句处理
	- 由于read_html()爬取table的单项td导致13项每一年的td都会重复显示（原因尚未不明），导致不美观也不方便我后续使用该数据，所以使用drop()方法删除
- 未来会优化/完善的地方：爬取方式改为多线程，使用pandas讲数据写入excel，

*鄙人为python初学者，为了方便查看理解，所有的细节都做了注释。如果有大神对这个感兴趣可联系鄙人，QQ：746139767 （大神麻烦备注CSDN）*
*项目源码、静态网页以及爬取的txt文件已上传Github:*
> https://github.com/LorentzForceWorkEnzyme/Demo_Crawler/tree/master/1.4%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%89%A7%E9%9B%86%E4%BF%A1%E6%81%AF%E8%A1%A8%E7%88%AC%E5%8F%96
