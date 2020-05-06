# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:10:39 2019

@author: reddymv
"""

import webbrowser
import tkinter as tk
from tkinter import *
Facebook = 'https://www.facebook.com'
Instagram ='https://www.instagram.com'
Linkedin = 'https://www.linkedin.com'
Twitter = 'https://www.twitter.com'
Amazon = 'https://www.amazon.com'

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
    

button1 = Button(window, text="Facebook", command=OpenUrl1, pady=10, fg = "blue", height=3, width =15)

button2 = Button(window, text="Instagram", command=OpenUrl2, pady=10, fg = "blue", height=3, width =15)

button3 = Button(window, text="Linkedin", command=OpenUrl3, pady=10, fg = "blue", height=3, width =15)

button4 = Button(window, text="Twitter", command=OpenUrl4, pady=10, fg = "blue", height=3, width =15)

button5 = Button(window, text="Amazon", command=OpenUrl5, pady=10, fg = "blue", height=3, width =15)

button1.grid( padx = 30, pady = 10, column=1, row =0)

button2.grid( pady = 10, column=1, row =1)

button3.grid(pady=10, column=1, row =2)

button4.grid( pady=10, column=1, row =3)

button5.grid(pady=10, column=1, row =4)

window.mainloop()
