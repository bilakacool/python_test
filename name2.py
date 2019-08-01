# # coding=utf-8
# # my_name = 'chenmo'
# # print(my_name[-6])
# # for i in my_name:
# #     print(i,end=' ')
#
# # a = a.replace('e', 'c', 10)
# # print(a)
#
# # if a == a[::-1]:
# #     print('OK')
# # else:
# #     print('错了')
#
# # a = "chen@mo@163.com"
# # if a.count('@') != 1:
# #     print('邮箱不合法')
# # else:
# #     # print('用户名：', a[:a.find('@')], '\n邮箱后缀：', a[a.find('@')+1:])
# # print('用户名：', a.split('@')[0], '\n邮箱后缀：', a.split('@')[1])
#
# # a = [[1], [2], [3], 'as']
# # for i in a:
# #     for j in i:
# #         print(j)
#
# # a = a[::-1]
# # print(a)
# # import random
# # a = []
# # for i in range(10):
# #     a.append(random.randint(1, 100))
# # print(a)
# # for i in range(10):
# #     for j in range(10):
# #         if a[i] < a[j]:
# #             a[i], a[j] = a[j], a[i]
# # print(a)
#
# # a = 'adf'
# # print(list(a))
# #
# # a = [['a1', '3'], ['3b', '2'], ['24', '1']]
# # a[1].sort(reverse=True)
# # print(a)
#
#
# # from PyQt5 import QtCore, QtGui, QtWidgets, Qt
# # from PyQt5.QtWidgets import *
# # from PyQt5.QtCore import *
# #
# #
# # class Ui_MainWindow(QtWidgets.QMainWindow):
# #
# #     def __init__(self):
# #         super(Ui_MainWindow,self).__init__()
# #         self.setupUi(self)
# #         self.retranslateUi(self)
# #
# #     def setupUi(self, MainWindow):
# #         MainWindow.setObjectName("MainWindow")
# #         MainWindow.resize(386, 127)
# #         self.centralWidget = QtWidgets.QWidget(MainWindow)
# #         self.centralWidget.setObjectName("centralWidget")
# #         self.retranslateUi(MainWindow)
# #
# #         self.pushButton = QtWidgets.QPushButton(self.centralWidget)
# #         self.pushButton.setGeometry(QtCore.QRect(190, 90, 75, 23))
# #         self.pushButton.setObjectName("pushButton")
# #         self.pushButton.setText("打开")
# #         MainWindow.setCentralWidget(self.centralWidget)
# #         QtCore.QMetaObject.connectSlotsByName(MainWindow)
# #
# #         self.pushButton.clicked.connect(self.openfile)
# #
# #     def retranslateUi(self, MainWindow):
# #         _translate = QtCore.QCoreApplication.translate
# #         MainWindow.setWindowTitle(_translate("MainWindow", "一颗数据小白菜"))
# #
# #     def openfile(self):
# #         openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xlsx , *.xls)')
# #
# #
# # if __name__ == "__main__":
# #     import sys
# #     app = QtWidgets.QApplication(sys.argv)
# #     MainWindow = QtWidgets.QMainWindow()
# #     ui = Ui_MainWindow()
# #     ui.setupUi(MainWindow)
# #     MainWindow.show()
# #     sys.exit(app.exec_())
#
# # from Tkinter import *
# # from FileDialog import *
# # root = Tk()
# # fd = LoadFileDialog(root)  # 创建打开文件对话框
# # filename = fd.go()  # 显示打开文件对话框，并获取选择的文件名称
# # print(filename)
# # root.mainloop()
#
# # import win32ui
# # dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
# # dlg.SetOFNInitialDir('E:/Python')  # 设置打开文件对话框中的初始显示目录
# # dlg.DoModal()
# # filename = dlg.GetPathName()  # 获取选择的文件名称
# # print(filename)
#
# # from tkinter.filedialog import askdirectory
# # a = askdirectory()
# # print(a)
# #
# # import win32ui
# # dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
# # dlg.SetOFNInitialDir('E:/Python')  # 设置打开文件对话框中的初始显示目录
# # dlg.DoModal()
# # dlg.GetPathName()  # 获取选择的文件名称
#
#
# import tkinter, time, decimal, math, string
#
# root = tkinter.Tk()
# root.title('计算器')
# root.resizable(0, 0)
# global cuncu, vartext, result, fuhao
# result = fuhao = None
# vartext = tkinter.StringVar()
# cuncu = []
#
#
# class anjianzhi:
#     global cuncu, vartext, result, fuhao
#
#     def __init__(self, anjian):
#         self.anjian = anjian
#
#     def jia(self):
#         cuncu.append(self.anjian)
#         vartext.set(''.join(cuncu))
#
#     def tui(self):
#         cuncu.pop()
#         vartext.set(''.join(cuncu))
#
#     def clear(self):
#         cuncu.clear()
#         vartext.set('')
#         result = None
#         fuhao = None
#
#     def zhengfu(self):
#         if cuncu[0]:
#             if cuncu[0] == '-':
#                 cuncu[0] = '+'
#             elif cuncu[0] == '+':
#                 cuncu[0] = '-'
#             else:
#                 cuncu.insert(0, '-')
#         vartext.set(''.join(cuncu))
#
#     def xiaoshudian(self):
#         if cuncu.count('.') >= 1:
#             pass
#         else:
#             if cuncu == []:
#                 cuncu.append('0')
#             cuncu.append('.')
#             vartext.set(''.join(cuncu))
#
#     def yunshuan(self):
#         global cuncu, vartext, result, fuhao
#         if vartext.get() == '':
#             pass
#         else:
#             get1 = decimal.Decimal(vartext.get())
#             if self.anjian in ('1/x', 'sqrt'):
#                 if self.anjian == '1/x':
#                     result = 1 / get1
#                 elif self.anjian == 'sqrt':
#                     result = math.sqrt(get1)
#             elif self.anjian in ('+', '-', '*', '/', '='):
#                 if fuhao is not None:
#                     get1 = decimal.Decimal(result)
#                     get2 = decimal.Decimal(vartext.get())
#                     if fuhao == '+':
#                         result = get1 + get2
#                     elif fuhao == '-':
#                         result = get1 - get2
#                     elif fuhao == '*':
#                         result = get1 * get2
#                     elif fuhao == '/':
#                         result = get1 / get2
#                 else:
#                     result = get1
#                 if self.anjian == '=':
#                     fuhao = None
#                 else:
#                     fuhao = self.anjian
#             print(fuhao)
#             print(result)
#             vartext.set(str(result))
#             cuncu.clear()
#
#
# def copy1():
#     # tkinter.Misc().clipboard_clear()
#     tkinter.Misc().clipboard_append(string(vartext.get()))
#
#
# def buju(root):
#     global cuncu, vartext, result, fuhao
#     entry1 = tkinter.Label(root, width=30, height=2, bg='white', anchor='se', textvariable=vartext)
#     entry1.grid(row=0, columnspan=5)
#     buttonMC = tkinter.Button(root, text='MC', width=5)
#     buttonMR = tkinter.Button(root, text='MR', width=5)
#     buttonMS = tkinter.Button(root, text='MS', width=5)
#     buttonM1 = tkinter.Button(root, text='M+', width=5)
#     buttonM2 = tkinter.Button(root, text='M-', width=5)
#     buttonMC.grid(row=1, column=0)
#     buttonMR.grid(row=1, column=1)
#     buttonMS.grid(row=1, column=2)
#     buttonM1.grid(row=1, column=3)
#     buttonM2.grid(row=1, column=4)
#
#     buttonJ = tkinter.Button(root, text='←', width=5, command=anjianzhi('c').tui)
#     buttonCE = tkinter.Button(root, text='CE', width=5)
#     buttonC = tkinter.Button(root, text=' C ', width=5, command=anjianzhi('c').clear)
#     button12 = tkinter.Button(root, text='±', width=5, command=anjianzhi('c').zhengfu)
#     buttonD = tkinter.Button(root, text='√', width=5, command=anjianzhi('sqrt').yunshuan)
#     buttonJ.grid(row=2, column=0)
#     buttonCE.grid(row=2, column=1)
#     buttonC.grid(row=2, column=2)
#     button12.grid(row=2, column=3)
#     buttonD.grid(row=2, column=4)
#
#     button7 = tkinter.Button(root, text=' 7 ', width=5, command=anjianzhi('7').jia)
#     button8 = tkinter.Button(root, text=' 8 ', width=5, command=anjianzhi('8').jia)
#     button9 = tkinter.Button(root, text=' 9 ', width=5, command=anjianzhi('9').jia)
#     buttonc = tkinter.Button(root, text=' / ', width=5, command=anjianzhi('/').yunshuan)
#     buttonf = tkinter.Button(root, text=' % ', width=5)
#     button7.grid(row=3, column=0)
#     button8.grid(row=3, column=1)
#     button9.grid(row=3, column=2)
#     buttonc.grid(row=3, column=3)
#     buttonf.grid(row=3, column=4)
#
#     button4 = tkinter.Button(root, text=' 4 ', width=5, command=anjianzhi('4').jia)
#     button5 = tkinter.Button(root, text=' 5 ', width=5, command=anjianzhi('5').jia)
#     button6 = tkinter.Button(root, text=' 6 ', width=5, command=anjianzhi('6').jia)
#     buttonx = tkinter.Button(root, text=' * ', width=5, command=anjianzhi('*').yunshuan)
#     buttonfs = tkinter.Button(root, text='1/x', width=5, command=anjianzhi('1/x').yunshuan)
#     button4.grid(row=4, column=0)
#     button5.grid(row=4, column=1)
#     button6.grid(row=4, column=2)
#     buttonx.grid(row=4, column=3)
#     buttonfs.grid(row=4, column=4)
#
#     button1 = tkinter.Button(root, text=' 1 ', width=5, command=anjianzhi('1').jia)
#     button2 = tkinter.Button(root, text=' 2 ', width=5, command=anjianzhi('2').jia)
#     button3 = tkinter.Button(root, text=' 3 ', width=5, command=anjianzhi('3').jia)
#     button_ = tkinter.Button(root, text=' - ', width=5, command=anjianzhi('-').yunshuan)
#     buttondy = tkinter.Button(root, text=' \n = \n ', width=5, command=anjianzhi('=').yunshuan)
#     button1.grid(row=5, column=0)
#     button2.grid(row=5, column=1)
#     button3.grid(row=5, column=2)
#     button_.grid(row=5, column=3)
#     buttondy.grid(row=5, column=4, rowspan=2)
#
#     button0 = tkinter.Button(root, text='   0   ', width=11, command=anjianzhi('0').jia)
#     buttonjh = tkinter.Button(root, text=' . ', width=5, command=anjianzhi('c').xiaoshudian)
#     buttonjia = tkinter.Button(root, text=' + ', width=5, command=anjianzhi('+').yunshuan)
#     button0.grid(row=6, column=0, columnspan=2)
#     buttonjh.grid(row=6, column=2)
#     buttonjia.grid(row=6, column=3)
#
#
# def caidan(root):
#     menu = tkinter.Menu(root)
#     submenu1 = tkinter.Menu(menu, tearoff=0)
#     menu.add_cascade(label='查看', menu=submenu1)
#     submenu2 = tkinter.Menu(menu, tearoff=0)
#     submenu2.add_command(label='复制')
#     submenu2.add_command(label='粘贴')
#     menu.add_cascade(label='编辑', menu=submenu2)
#     submenu = tkinter.Menu(menu, tearoff=0)
#     submenu.add_command(label='查看帮助')
#     submenu.add_separator()
#     submenu.add_command(label='关于计算机')
#     menu.add_cascade(label='帮助', menu=submenu)
#     root.config(menu=menu)
#
#
# buju(root)
# caidan(root)
# root.mainloop()

# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))
