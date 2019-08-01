# coding=utf-8

# test_id = 0
# user_name = 'admin'
# user_pass = '123456'
#
# while test_id == 0:
#     for test_id2 in range(3):
#         input_name = input('请输入用户名：')
#         if input_name == user_name:
#             test_id = 2
#             while test_id == 2:
#                 for test_id3 in range(3):
#                     input_pass = input('请输入密码：')
#                     if input_pass == user_pass:
#                         print('登录成功')
#                         test_id = 1
#                     else:
#                         print('密码错误，请重新输入')
#                 print('密码三次输入错误，请退出')
#                 break
#
#         else:
#             print('用户名输入错误，请重新输入')
#     print('用户三次输入错误，请退出')


# a = [(3,), 3, [3], '3']
# a[0] = 3
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# b = a[:]
# c = a
# print(id(a), id(b), id(c))

# a = {1:1,2:2}
# b = a
# print(id(a), id(b))

# a = 'c://a/b/c'
# a = a.split('/')[:-1]
# print('{a}{a}{c}'.format(a=1, c=3))
# print('{a}{a}{c}')

# 引入日历模块
# import calendar
#
# # 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))
#
# # 显示日历
# print(calendar.month(yy, mm))

# a = [3, 5, 1, 8, 2, 4, 7, 9, 3]
# b = []
# i = 0
# while a == []:
#     b.insert(i, min(a))
#     a.remove(min(a))
#     i += 1
# a = b
# print(a)

# def a(a):
# print(map(a(3),5))

# def jiecheng(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jiecheng(n-1)
#
# print(jiecheng(5))


# def feb(n):
#     if n < 1:
#         return
#     elif n <= 2:
#         return 1
#     else:
#         return feb(n-2)+feb(n-1)
#
#
# print(feb(2))

# def hanoi(n, x='x', y='y', z='z'):
#     if n == 1:
#         print(x, '-->', z)
#     else:
#         hanoi(n-1, x, z, y)
#         hanoi(1)
#         hanoi(n-1, y, x, z)
# hanoi()

# print(dict([['a', 1]]))
#
# print(dict(a=1, b=2))

# a = {1,2}
# print(type(a))

import os
# a = open('C:\\Users\\lajidiannao\\Desktop\\新建文本文档.txt', 'r')
# a.read(1)
# print(a.tell())
# a.seek(1, 1)
# print(a.read(1))

# print(os.getcwd())
# os.chdir('C:/Users/lajidiannao/Desktop')
#
# os.makedirs('a/b')
# os.removedirs('a/b')
# os.system('notepad')
# print(os.path.basename('C:/a/a/'))


# print(os.path.splitext('a/a/a/a.txt'))
import pickle
# b = ['陈墨', 2, 3]
# a = open('a.as', 'wb')
# pickle.dump(b, a)
# a.close()
# a = open('a.as','rb')
# b = pickle.load(a)
# a.close()
#
# print(b)
# b = open('yonghu.yonghu', 'rb')
# a = pickle.load(b)
# print(a.items())
# if ('陈墨','123456') not in a.items():
#     print(1)

# from easygui import *
# import sys
# while 1:
#     msgbox('欢迎进入第一个界面小游戏')
#     msg = '你想学习什么'
#     title = '小游戏互动'
#     choices = ['谈恋爱', '编程', '琴棋书画']
#     choice = choicebox(msg, title, choices)
#     msgbox('你的选择是：' + str(choice), '结果')
#     msg = '重新开始吗'
#     title = '请选择'
#     if ccbox(msg, title):
#         pass
#     else:
#         sys.exit(0)

# class B1:
#     def f2(self):
#         print(1)
# class B2:
#     def f2(self):
#         print(2)
# class C(B2,B1):
#     pass
# c = C()
# c.f3()
# import time
# for i in range(5000):
#     os.system('C:\\Users\\lajidiannao\\Desktop\\新建文本文档.bat')
#     time.sleep(1)
#     os.system('C:\\Users\\lajidiannao\\Desktop\\新建文本文档 - 副本.bat')
#     time.sleep(1)
#     os.system('C:\\Users\\lajidiannao\\Desktop\\新建文本文档 - 副本 - 副本.bat')
# import easygui as g
#
# # g.msgbox("Hello Easy GUI")
# # g.msgbox(msg="我一定要学会编程！",title="标题部分",ok_button="加油")
# # g.ccbox("亲爱的还玩吗?",choices=("还要玩！","算了吧/(ㄒoㄒ)/~~"))
# # g.msgbox("还是不玩了，快睡觉吧！")
#
# msg = "请填写一下信息(其中带*号的项为必填项)"
# title = "账号中心"
# fieldNames = ["*用户名","*真实姓名","固定电话","*手机号码","QQ","*Email"]
# fieldValues = g.multenterbox(msg, title, fieldNames)
# print(fieldValues)
# while True:
#     if fieldValues == None :
#         break
#     errmsg = ""
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == "" and option[0] == "*":
#             errmsg += ("【%s】为必填项   " %fieldNames[i])
#     if errmsg == "":
#         break
#     fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
# print("您填写的资料如下:%s" %str(fieldValues))


# class Ta:
#     """123456"""
#
#     ming = 'g'
#     __zi = 'h'
#
#     def __init__(self, color='a', name='b'):
#         self.color = color
#         self.name = name
#
#     def zoulu(self):
#         print(self.color, Ta.ming, Ta.__zi, Ta.__doc__)
#
#     def __del__(self):
#         print('123')
#
#     def __add__(self, b):
#         print('321')
#
# a = Ta()
# b = Ta('e', 'f')
# a.__init__('c', 'd')
# a.zoulu()
# b.zoulu()

# print(setattr(a, 'name3', '2'))
# delattr(a, 'name3')
# print(getattr(a, 'name3', '不存在'))

# print(a.name+'b')


# class A:
#     def __init__(self, b=10, f=20):
#         self.b = b
#         self.f = f
#     def getattr(self):
#         return self.f
#     def setattr(self, value):
#         self.b = value
#         self.f = value
#     def delattr(self):
#         del self.b
#     c = property(getattr, setattr, delattr)
# d = A()
# print(d.c)
# d.c = 1
# print(d.c)
# del d.c
# print(d.f)

# a = [x for x in '132']
# b = list('132')
# print(a, b)
# c = iter(a)
# print(next(iter(a)))
# print(next(iter(a)))
# print(next(iter(a)))
# print(next(c))

# import urllib.request
#
# response = urllib.request.urlopen("http://placekitten.com/g/500/600")
# html = response.read()
# with open('C:\\Users\\lajidiannao\\Desktop\\a.jpg', 'wb') as f:
#     f.write(html)


# import re
# a = re.search(r'as$', 'a456212125s')
# b = re.findall(r'\s{', 'cbaacac')
# print(b)
#
# import math
# print(math.sin(math.pi/4))
#
# import random
# print(random.sample('adf', 3))
# b = [1, 5, 6]
# random.shuffle(b)
# print(b)

# import glob
# print(glob.glob('*.py'))

# import time
# from datetime import date
# print(time.strftime('%m', time.localtime()))
# a = date(2000, 1, 1)
# print(a.strftime('%M'))

# import sys
# print(sys.platform)


# import sys
# import time
# print(1)
# print('\rasfa',end='')
# time.sleep(1)
#
# print('\r2',end = '')
# time.sleep(1)
# print('\r3')
# sys.stdout.write('a')

# from urllib import request
# url = 'http://www.baidu.com'
# url = request.Request(url)
# response = request.urlopen(url)
# print(response.read().decode('utf-8'))
# print(response.getheader('P3p'))

# import json
# from urllib import request, parse
# import easygui as g

# g.msgbox('打开有道翻译')
# while 1:
#         i = g.enterbox('请输入要翻译的内容')
#         if i is None:
#                 break
#         url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#
#         data = {'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb', 'salt': '15645652799174',
#                  'sign': '01cee8eb29b5288d41417d4fba17b558', 'ts': '1564565279917', 'bv': '6e48c00e5938573284960d43e8a021fd',
#                  'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME', 'i': i}
#         data = parse.urlencode(data).encode('utf-8')
#
#         headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'}
#         req = request.Request(url, data, headers, method='POST')
#
#         response = request.urlopen(req)
#         a = response.read().decode('utf-8')
#
#         a = json.loads(a)
#         a = a['translateResult'][0][0]['tgt']+'：'+a['translateResult'][0][0]['src']
#         g.msgbox('%s的翻译结果为：%s' % (i, a))

# from urllib import request, parse
# url = 'http://www.whatismyip.com.tw'
# ip = {'http':'60.188.38.186:9000'}
# proxy_support = request.ProxyHandler(ip)
# opener = request.build_opener(proxy_support)
# request.install_opener(opener)
# response = request.urlopen(url)
# a = response.read().decode('utf-8')
# print(a)

# for i in range(10,0,-1):
#         print(i)

# from urllib import request, parse
# import os
#
# def url_open(url):
#         req = request.Request(url)
#         req.add_header('User-Agent',
#                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400')
#         response = request.urlopen(url)
#         html = response.read()
#         return html
#
# def get_page(url):
#         html = url_open(url).decode('utf-8')
#
#         a = html.find('current-comment-page') + 23
#         b = html.find(']', a)
#         return html[a:b]
#
# def find_imgs(url):
#         html = url_open(url).decode('utf-8')
#         img_addrs = []
#
#         a = html.find('img src=')
#
#         while a != -1:
#                 b = html.find('.jpg', a, a+255)
#                 if b != -1:
#                         img_addrs.append(html[a+9:b+4])
#                 else:
#                         b = a+9
#                 a = html.find('img src', b)
#
#         return img_addrs
#
# def save_imgs(img_addrs):
#         for each in img_addrs:
#                 filename = each.split('/')[-1]
#                 with open(filename, 'wb') as f:
#                         img = url_open(each)
#                         f.write(img)
#
# def bizhi(folder='C:\\Users\\lajidiannao\\Desktop\\ooxx', pages=10):
#         from fuzhi import shanchu
#         shanchu(folder)
#         os.mkdir(folder)
#         os.chdir(folder)
#
#         url = 'http://jandan.net/ooxx/'
#         page_num = int(get_page(url))
#
#         for i in range(pages):
#                 page_num -= i
#                 page_url = url+ '/'+'page'+ str(page_num)+'#comments'
#                 img_addrs = find_imgs(page_url)
#                 save_imgs(img_addrs)
#
# if __name__ == '__main__':
#         bizhi()

from tkinter import *
from time import sleep
root = Tk()             #生成root主窗口
root.title('标题')               #设置标题
# root.resizable(100,8000)
root.geometry('1000x800')       #设置窗口大小

# sleep(2)
# root.quit()
# sleep(2)
# root.update()
v1 = StringVar()
a1 = Label(root,textvariable=v1, bg='green', font=('Arial', 12), width=30, height=2)
a1.pack()                        #添加标签到窗口
v1.set('未点击')
dian = False
def dianji():
        global dian
        if not dian:
                dian = True
                v1.set('已点击')
        else:
                dian = False
                v1.set('未点击')

b1 = Button(root,text='Yes',command=dianji)
b1.pack()               #添加按钮

e1 = Entry(root, show='*')
e1.pack()

def shuru1():
        v1.set(e1.get())

b3 = Button(root, text='shuru1',command=shuru1)
b3.pack()


t1 = Text(root,height=3)
t1.pack()

def shuru2():
        v1.set(t1.get('0.0','2.0'))

b4 = Button(root, text='shuru2',command=shuru2)
b4.pack()

v2 = StringVar()
l1 = Listbox(root, listvariable=v2, height=5)
v2.set(('11','22','33'))
l1.insert(1,'55')
l1.delete(1)
l1.pack()

def xuanze():
        v1.set(l1.get(l1.curselection()))

b2 = Button(root, text='xuanze',command=xuanze)
b2.pack()


r1 = Radiobutton(root,text='aA',variable=v1,value='A')
r1.pack()
r2 = Radiobutton(root,text='bB',variable=v1,value='B')
r2.pack()


def xuanze3():
        if (v3.get() == 1) & (v4.get() == 0):
                v1.set('我喜欢足球')
        elif (v3.get() == 0) & (v4.get() == 1):
                v1.set('我喜欢篮球')
        elif (v3.get() == 1) & (v4.get() == 1):
                v1.set('我喜欢足球和篮球')
        else:
                v1.set('我不喜欢球')

v3 = IntVar()
v4 = IntVar()

c1 = Checkbutton(root, text='足球', variable=v3, onvalue=1, offvalue=0,command=xuanze3)
c2 = Checkbutton(root, text='篮球', variable=v4, onvalue=1, offvalue=0,command=xuanze3)
c1.pack()
c2.pack()

# b3 = Button(root, text='xuanze3', command=xuanze3)
# b3.pack()

# def xuanze4(v):
#       v1.set('选择的是'+v)
#
# s1 = Scale(root, label= '最小值', from_=0, to=10, orient=HORIZONTAL, length=200, showvalue=, tickinterval=2, resolution=0.1,command=xuanze4)
# s1.pack()





root.mainloop()                 #打开窗口
























