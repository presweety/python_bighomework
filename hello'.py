# -*- coding: utf-8 -*-
'''
# __author__ = 'DELL'
'''
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from url import lunar


class visual(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.master = window
        self.pack()
        self.date = tk.StringVar()
        window.geometry('500x300')
        window.title('中国老黄历查询窗口')

        self.intWind()

    def buttonActive(self):
        p = self.date.get()
        tmp = lunar(p)
        data = tmp.GetDataFromAPI()
        data1 = data['newslist'][0]
        #       print(data['newslist'][0]['name'])
        #       if data == {}:
        #         messagebox.showinfo('查询结果','not found')
        #       else:
        messagebox.showinfo('查询结果', '农历日期:' + str(data1['lunardate'])+
                            '\n干支纪年，月，日:  ' + str(data1['tiangandizhiyear']) + str(data1['tiangandizhimonth']) + str(data1['tiangandizhiday']) +
                            '\n季节:' + str(data1['lmonthname']) + '\n生肖:' + str(data1['shengxiao']) +
                            '\n农历节日: ' + str(data1['lunar_festival']) +'\n公历节日: ' + str(data1['festival']) +
                            '\n宜:' + str(data1['fitness']) +'\n忌:' + str(data1['taboo']) +'\n吉神方位:' + str(data1['shenwei']) +
                            '\n胎神: ' + str(data1['taishen']) +'\n冲煞:' + str(data1['chongsha']) + '\n岁煞:' + str(data1['suisha']) +
                            '\n星宿:  ' + str(data1['xingsu']) +'\n彭祖百忌:  ' +str(data1['pengzu'])+
                            '\n建星:' +str(data1['jianshen'])+'\n节气:' +str(data1['jieqi']))
        #       print('\n')
        #       print(type(data))
        #       messagebox.showinfo('',data)
        return

    def intWind(self):
        frame1 = Frame(self)
        Label(frame1, text='请输入一个公历日期').grid(row=0, column=0)
        Entry(frame1, textvariable=self.date).grid(row=0, column=1)
        frame1.grid(pady=10)
        Button(self, text='确定', width=15, command=self.buttonActive).grid(pady=5)


if __name__ == '__main__':
    window = tk.Tk()
    application = visual(window)
    application.mainloop()

