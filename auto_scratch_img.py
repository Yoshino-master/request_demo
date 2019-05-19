'''
Created on 2019年5月19日

@author: jinglingzhiyu
'''
import re, pickle, requests, os, time
#from frame_of_wing.other_tools.reptile import getHTMLText

def getHTMLText(url, timeout=50):
    try:
        r = requests.get(url, timeout=timeout)      #获取url网页对象
        r.raise_for_status()                        #判断是否产生异常
        r.encoding = r.apparent_encoding            #改变编码方式
        return r.text                               #返回网页内容(以字符串形式)
    except:
        return "Request Error"

def download_img(html, save_root, Num=3):
#下载图片,真实图片数为Num*30
    if os.path.exists(save_root) is False:
        os.mkdir(save_root)
    finder = re.compile(r'https://.*?gp=0.jpg')
    res = finder.findall(html)
    res = list(set(res))          #列表元素去重
    count = 0
    for j in range(Num):
        for i in range(len(res)):
            url = res[i] + '&pn=' + str(j + 1)
            r = requests.get(url)
            r.raise_for_status()
            with open(save_root + '//' + str(count) + '.png', 'wb') as f:
                f.write(r.content)
            time.sleep(0.3)
            count += 1
    
def demo_scratch():
    keyword = '兔子'
    url_template = r'https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word=待替换&oq=待替换'
    url = url_template.replace('待替换', keyword)
    html = getHTMLText(url)
    save_root = r'imgs'
    if os.path.exists(save_root) is False:
        os.mkdir(save_root)
    save_root = os.path.join(save_root, keyword)
    if os.path.exists(save_root) is False:
        os.mkdir(save_root)
    download_img(html, save_root)

if __name__ == '__main__':
    demo_scratch()
