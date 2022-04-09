# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:32:03 2022

@author: DELL
"""

from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.title("List")
root.configure(background = "lightblue")
label1 = Label(root , fg = "black" , bg = "lightgreen")
label1.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)

label2 = Label(root , fg = "black" , bg = "lightgreen")
label2.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)

label3 = Label(root , text = "Random Gift Chooser" , fg = "black" , bg = "lightgreen" , font = ("italic" , 20))
label3.place(relx = 0.5 , rely = 0.1 , anchor = CENTER)

giftlist = ["Hanky" , "Bottle" , "Tiffin" , "Chocolate" , "Chips"]

label1['text']= "Listed Items: " + str(giftlist)

def run():
    r = random.sample(range(1,6) , 1)
    label2['text'] = "Put Item No. " + str(r) + " in Bag"

btn = Button(root , text = "Which item to put in bag?" , fg = "black" , bg = "orange" , command = run)
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
root.mainloop()