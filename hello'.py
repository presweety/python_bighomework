# -*- coding: utf-8 -*-
'''
# __author__ = 'DELL'
'''
import tkinter as tk
from tkinter import *     #thus we can use its function
from tkinter import messagebox
from url import lunar


class visual(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.master = window
        self.pack()
        self.date = tk.StringVar(None,'xxxx_xx_xx')
        window.geometry('500x300')
        window.title('中国老黄历查询窗口')

        self.intWindow()

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

    def intWindow(self):
        frame1 = Frame(self)
        Label(frame1, text='请输入一个公历日期',font=('Courier',15)).grid(row=0, column=0)   #add font setting
        Entry(frame1, textvariable=self.date,font=('Courier',15)).grid(row=1, column=1)
        frame1.grid(pady=10)
        Button(self, text='确定', width=15,font=('Courier',15), command=self.buttonActive).grid(pady=5)


if __name__ == '__main__':
    window = tk.Tk()


    Canvas = tk.Canvas(window, height=100, width=100)  #add window background
    Canvas.pack()

    background_image = tk.PhotoImage(file='D:\hhhh.png')
    background_label = tk.Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    application = visual(window)
    application.mainloop()

