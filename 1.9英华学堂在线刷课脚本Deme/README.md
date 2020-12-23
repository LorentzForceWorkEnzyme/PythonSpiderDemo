 <center><font color=#DC143C size=6> 警告 FBI WARNING</font></center>

![警告](https://img-blog.csdnimg.cn/20201223122306992.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM3NTM1Ng==,size_12,color_FFFFFF,t_70#pic_center)

<font color=#DC143C size=6 face="黑体">此文章仅供学习参考，请勿使用在教学网站使用！！！</font>
<font color=#DC143C size=6 face="黑体">此文章仅供学习参考，请勿使用在教学网站使用！！！</font>
<font color=#DC143C size=6 face="黑体">此文章仅供学习参考，请勿使用在教学网站使用！！！</font>

---
# 使用Tampermonkey油猴挂载JS脚本，实现自动化播放课程。目前脚本未完全实现，仅学习使用。
>*URL*：[英华学堂](*http://mooc.yinghuaonline.com/*)
>Module：JavaScript 、chrome、Tampermonkey油猴
>Status：未完成，Demo Version1.0
>@Author：xiaozhu_sai
>Date:2020/12/22

**目标课程**:![在这里插入图片描述](https://img-blog.csdnimg.cn/20201223122121616.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM3NTM1Ng==,size_5,color_FFFFFF,t_70#pic_center)
**脚本代码（功能未能完整实现）：**
```javascript
//@Author:xiaozhu_sai
//Date:2020/12/22
//url = 'http://mooc.yinghuaonline.com/
//初始准备，点开第一章第一节界面


document.evaluate('/html/body/div[5]', document).iterateNext().style.display = 'none'
//定位课程目录
var group = document.getElementsByClassName('group two ');
//课程章节 item
window.unit = 0;

//执行一次/3s
function start(){
    //获取当前页面video元素
    var video = document.getElementsByTagName('video');

    //获取当前章小节列表 38节
    //定位课程目录 test
    var group = document.getElementsByClassName('group two ');
    var navlist = document.getElementsByClassName('detmain-navlist')[0];
    var item = navlist.getElementsByClassName('item');
    //展开所有章节
    for (i=0;i<group.length;i++){group[i].className = "group two on"; }

    //空页面, 跳转下一章
    if (video.length == 0){
        //章节加一
        window.unit += 1;
        
        //下一节
        item[window.unit].getElementsByTagName('a')[0].click();
    }
    //视频已播放完
    if(video[0].ended == true){
        //章节加一
        window.unit += 1;

        //下一节
        item[window.unit].getElementsByTagName('a')[0].click();
    }
    //未观看&未看完的视频，播放
    if (video[0].paused == true && video[0].ended == false){
        //静音
        video[0].volume = 0;
        //开始播放当前视频
        video[0].play();
        // //测试 加速播放
        // video[0].playbackRate = 8;
    }
    console.log('start ',i++, window.unit)

    //监听播放结束
    //Todo:因为网络原因暂停-事件
    //video[0].addEventListener('ended', function(){foo(video, item);}, false);
}

var i = 1
//每分钟执行一次
setInterval(start, 1*1000);


```


## 功能分析：
- 播放每一节的视频，存在空页面章节（测验章节）
- 后台判断课程是否观看完成，是看在视频页面**停留时间**，所以无法单纯使用playbackRate加速播放解决。
- 当前视频播放完，点击进入下一章节
- 在中间章节时，会弹出验证码对话框。由于警告，无法使用python（selenium）/OCR识别解决。
- 由于点击章节页面刷新，控制台脚本失效。使用油猴脚本浏览器插件运行脚本
## 功能实现&未实现
### [ √ ] 已实现
- 运行脚本后，自动检测并播放视频。
- 播放完后自动跳转到下一章节

###  [ X ] 未实现
- 遇到空章节（空页面），脚本自动关闭
- 章节低频跳出的验证码，未实现自动识别通过
- 因网络原因可能导致视频暂停，等待，直到网络良好后继续播放课程
## 步骤

1. 安装油猴插件，推荐使用Chrome或FireFox（Edge Opera）
[欢迎来到 Greasy Fork，这里是一个提供用户脚本的网站。](https://greasyfork.org/zh-CN/)
[https://www.tampermonkey.net/](https://www.tampermonkey.net/)


2.
如图操作插件
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201223125018753.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM3NTM1Ng==,size_8,color_FFFFFF,t_70#pic_center)
3. 将脚本头部改为
*狗xx狗为自己的课程第一章第一节的nodeId（见url）*
```javascript
// ==UserScript==
// @name         观看脚本 Ver1.0
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match       http://mooc.yinghuaonline.com/user/node?nodeId=狗XXXXXX狗
// @grant        none
// ==/UserScript==
空白处粘贴上述脚本代码
```
4. 开启脚本，刷新网页即可.
