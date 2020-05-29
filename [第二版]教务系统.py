#教务系统成绩查询第二版 #
## 功能简介 ##
#1. 通过requests库进行get操作得到登陆的验证码
#2. 将验证码和学号以及密码等表单提交给远端服务器
#3. 获取此时cookies作为后续登陆的所以cookies
#4. 通过成绩查询页面post请求在校学习成绩的页面并保存

## 程序缺陷 ##
#1. 验证码未实现自动识别（或躲避验证码功能未设计）
#2. 没有实现对保存的成绩页面进行数据分析和处理

## 程序改进措施 ##
#1. 加入验证码躲避功能
#2. 对保存的成绩页面进行数据分析和处理
#3. 将数据以txt和excel文件保存下来
#4. 是否可以进行成绩数据的比较和图表
#5. 绩点计算

#import os
#from lxml import etree
import requests
import http.cookiejar

def getfunction(url,headers,key):
    if key ==1:
        s =requests.session()
        url_responose = s.get(url, headers = headers)
        cooker = s.cookies
        return cooker,url_responose.text
    else:
        try:
            r = requests.get(url,headers = headers,timeout=50)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print("网络连接超时,请检查网络连接!\n")

def Htmlparse(html):
    pass#暂不使用该模块
    
def file_save(content):
    with open("ifo.html",'wb') as f:
        f.write(content)
        f.close()

def main():
    print("欢迎使用正方教务系统辅助工具\n作者:Dukeo@Hu\n感谢你的使用!!!")
    #信息构建模块
    ifo = {
        'xh':'',
        'xm':'',
        'gnmkdm':''
    }
    ifo['xh'] = input("请输入你的姓名:")
    ifo['xm'] = input("请输入你的学号:")

    inf_key={
        '个人信息':'N121501',
        '密码修改':'N121502',
        '辅修报名':'N121504',
        '学生预定教材':'N121505',
        '专业推荐课表查询':'N121601',
        '学生个人课表':'N121602',
        '成绩查询':'N121603',
        '选课查询':'N121612'
    }
    urls = {
        'start':'http://xx.xx.com/xx.aspx'   #更换为你的教务系统地址
    }

    link_key={
        '学生个人课表':'xskbcx.aspx?',
        '成绩查询':'xscj.aspx?',
        '个人信息':'xsgrxx.aspx?',
        '密码修改':'mmxg.aspx?',
        '辅修报名':'xsfxbm.aspx?',
        '学生预定教材':'xsxjc.aspx?'
    }

    #提交表头，里面的参数是电脑各浏览器的信息。模拟成是浏览器去访问网页。
    headers_1 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    }

    headers_2 = {
        'Host':'xxx.xx.xx.xx',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':'http://xxx.x.xx.xx/xs_main.aspx?xh=xxxxxx',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        #'Cookie':'ASP.NET_SessionId=ky4vhczmhhzxs2455ossex55',#最开始我用的是固定的cookies所以出现大量问题，最后我使用了自动获取才解决
        }
    headers_3 = {
        'Cache-Control':'max-age=0',
        'Connection':'Keep-Alive',
        'Content-Length':'1461',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'xx.x.xx.xxx',
        'Referer':'http://xx.x.xx.xx/xscj.aspx?xh=xxxxxx&xm=xxDA&gnmkdm=xxx',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Origin':'http://xxx.x.xxx.xx',
        'Upgrade-Insecure-Requests':'1',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate'
    }


    #程序开始
    cookers = http.cookiejar.CookieJar()
    cookers = getfunction(urls['start'], headers_1, key=1)
    print(cookers)
    while True:
        print("step 2:请输入你需要查询的内容\n")
        print("1.个人信息~2.密码修改~3.课表~4.成绩\n")
        key_number = eval(input("请输入你需要查询内容的数字码:"))
        if key_number == 1:
            ifo['gnmkdm']= inf_key['个人信息']
            headers_3['Referer'] = "http://xx.x.xx.xx/"+link_key['个人信息'] +"xh="+ifo['xh']+"&xm="+ifo['xm']+"&gnmkdm="+ifo['gnmkdm']
            break
        elif key_number == 2:
            ifo['gnmkdm']= inf_key['密码修改']
            headers_3['Referer'] = "http://xx.x.xx.xxx/"+link_key['密码修改'] +"xh="+ifo['xh']+"&xm="+ifo['xm']+"&gnmkdm="+ifo['gnmkdm']
            break

        elif key_number ==3:
            ifo['gnmkdm']= inf_key['学生个人课表']
            headers_3['Referer'] = "http://xx.xx.xx.xx/"+link_key['学生个人课表'] +"xh="+ifo['xh']+"&xm="+ifo['xm']+"&gnmkdm="+ifo['gnmkdm']
            break
        elif key_number == 4:
            ifo['gnmkdm']= inf_key['成绩查询']
            headers_3['Referer'] = "http://xx.xx.xx.xx/"+link_key['成绩查询'] +"xh="+ifo['xh']+"&xm="+ifo['xm']+"&gnmkdm="+ifo['gnmkdm']
            break
        else:
            print("暂不支持该功能,请重新输入!!")
            
    
    #url构建
    headers_2['Referer'] = "http://xx.xx.xx.xx/xs_main.aspx?xh="+ifo['xh']
    url = headers_3['Referer']
    print(url)
    #html_content,html_text = getfunction(url,headers_3,key=3,cook =cookers)
    r = requests.post(url,headers=headers_3,cookies=cookers)
    r.encoding = r.apparent_encoding
    html_content = r.content    
    #print(r.text)
    #页面保存
    file_save(html_content)
    print("详细信息已保存到当前文件夹,请查看:ifo.html\n")
    print("感谢你的使用,再见!.............")
        
main()

