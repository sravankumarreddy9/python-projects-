# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:10:39 2019

@author: reddymv
"""

import webbrowser
import tkinter as tk
from tkinter import *
Punch_in_page = 'https://www.facebook.com'
Dictionary ='https://www.instagram.com'
Inside_Amazon = 'https://www.linkedin.com'
Mytimeoff_portal = 'https://www.twitter.com'
Amazon_au = 'https://www.amazon.com'

window = Tk()
window.title('Website Links')
window.geometry("400x500")
window.grid()
def OpenUrl1():
    webbrowser.open_new(Punch_in_page)
def OpenUrl2():
    webbrowser.open_new(Dictionary)
def OpenUrl3():
    webbrowser.open_new(Inside_Amazon)
def OpenUrl4():
    webbrowser.open_new(Mytimeoff_portal)
def OpenUrl5():
    webbrowser.open_new(Amazon_au)
    

button1 = Button(window, text="Punch_in page", command=OpenUrl1, pady=10, fg = "blue", height=3, width =15)

button2 = Button(window, text="Dictionary", command=OpenUrl2, pady=10, fg = "blue", height=3, width =15)

button3 = Button(window, text="Inside Amazon", command=OpenUrl3, pady=10, fg = "blue", height=3, width =15)

button4 = Button(window, text="Mytimeoff portal", command=OpenUrl4, pady=10, fg = "blue", height=3, width =15)

button5 = Button(window, text="Amazon au site", command=OpenUrl5, pady=10, fg = "blue", height=3, width =15)

button1.grid( padx = 30, pady = 10, column=1, row =0)

button2.grid( pady = 10, column=1, row =1)

button3.grid(pady=10, column=1, row =2)

button4.grid( pady=10, column=1, row =3)

button5.grid(pady=10, column=1, row =4)

window.mainloop()
