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
