# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:46:50 2020

@author: Rakin
"""

from tkinter import*
root= Tk()
 
root.title("Simple Calculator")
e=Entry(root, borderwidth=5, width=35)
e.grid(row=0,column=0, padx=10, pady=10,columnspan=3)
 
def clickMe(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,current+str(number))

def add():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global sign
    sign="+"
    e.delete(0, END)

def sub():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global sign
    sign="-"
    e.delete(0, END)

def mul():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global sign
    sign="*"
    e.delete(0, END)
    
def div():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global sign
    sign="/"
    e.delete(0, END)

def clear():
    e.delete(0,END)
def equal():
    second_number=e.get()
    e.delete(0, END)
    if sign=="+":
        e.insert(0,f_num+int(second_number))
    elif sign=="-":
        e.insert(0,f_num-int(second_number))
    elif sign=="*":
        e.insert(0,f_num*int(second_number))
    elif sign=="/":
        e.insert(0,f_num/int(second_number))
    
        
    

 
button_1= Button(root, text="1", padx=40, pady=20, command=lambda:clickMe(1), bg="#30E3E9")
button_2= Button(root, text="2", padx=40, pady=20, command=lambda:clickMe(2), bg="#30E3E9")
button_3= Button(root, text="3", padx=40, pady=20, command=lambda:clickMe(3), bg="#30E3E9")
button_4= Button(root, text="4", padx=40, pady=20, command=lambda:clickMe(4), bg="#30E3E9")
button_5= Button(root, text="5", padx=40, pady=20, command=lambda:clickMe(5), bg="#30E3E9")
button_6= Button(root, text="6", padx=40, pady=20, command=lambda:clickMe(6), bg="#30E3E9")
button_7= Button(root, text="7", padx=40, pady=20, command=lambda:clickMe(7), bg="#30E3E9")
button_8= Button(root, text="8", padx=40, pady=20, command=lambda:clickMe(8), bg="#30E3E9")
button_9= Button(root, text="9", padx=40, pady=20, command=lambda:clickMe(9), bg="#30E3E9")
button_0= Button(root, text="0", padx=40, pady=20, command=lambda:clickMe(0), bg="#30E3E9")

button_add= Button(root, text="+", padx=40, pady=20, command=add, bg="#E4FF33")
button_sub= Button(root, text="-", padx=40, pady=20, command=sub, bg="#E4FF33")
button_mul= Button(root, text="*", padx=40, pady=20, command=mul, bg="#E4FF33")
button_div= Button(root, text="/", padx=40, pady=20, command=div, bg="#E4FF33")
button_eql= Button(root, text="=", padx=40, pady=20, command=equal, bg="#E4FF33")
button_clr= Button(root, text="clr", padx=40, pady=20, command=clear, bg="#E4FF33")
 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mul.grid(row=4, column=2)
button_div.grid(row=4, column=1)
button_eql.grid(row=5, column=1, columnspan=4)
button_clr.grid(row=6, column=1, columnspan=4)

 
root.mainloop()