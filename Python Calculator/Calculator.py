# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:46:50 2020

@author: Rakin
"""
import math
from tkinter import*
root= Tk()


root.configure(bg="#34495E")
root.title("My Calculator")
e = Entry(root, borderwidth=10, width=30)
e.grid(row=0,column=0, padx=25, pady=25,columnspan=4)
 
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
    
def sqr():
    first_number=e.get()
    e.delete(0, END)
    global f_num
    f_num=int(first_number)
    e.insert(0,f_num**2)
    
def sqrt():
    first_number=e.get()
    e.delete(0, END)
    global f_num
    f_num=int(first_number)
    e.insert(0,math.sqrt(f_num))

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
    
        
    

 
button_1= Button(root, text="1", padx=40, pady=20, command=lambda:clickMe(1), bg="#45B39D")
button_2= Button(root, text="2", padx=40, pady=20, command=lambda:clickMe(2), bg="#52BE80")
button_3= Button(root, text="3", padx=40, pady=20, command=lambda:clickMe(3), bg="#76D7C4")
button_4= Button(root, text="4", padx=40, pady=20, command=lambda:clickMe(4), bg="#2980B9")
button_5= Button(root, text="5", padx=40, pady=20, command=lambda:clickMe(5), bg="#3498DB")
button_6= Button(root, text="6", padx=40, pady=20, command=lambda:clickMe(6), bg="#85C1E9")
button_7= Button(root, text="7", padx=40, pady=20, command=lambda:clickMe(7), bg="#7D3C98")
button_8= Button(root, text="8", padx=40, pady=20, command=lambda:clickMe(8), bg="#A569BD")
button_9= Button(root, text="9", padx=40, pady=20, command=lambda:clickMe(9), bg="#BB8FCE")
button_0= Button(root, text="0", padx=40, pady=20, command=lambda:clickMe(0), bg="#E59866")
                 

button_add= Button(root, text="+", padx=39, pady=20, command=add, bg="#D7BDE2")
button_sub= Button(root, text="-", padx=40, pady=20, command=sub, bg="#AED6F1")
button_mul= Button(root, text="*", padx=40, pady=20, command=mul, bg="#ABEBC6")
button_div= Button(root, text="/", padx=40, pady=20, command=div, bg="#F9E79F")
button_sqr= Button(root, text="SQR", padx=32, pady=20, command=sqr, bg="#F8C471")
button_sqrt= Button(root, text="SQRT", padx=28, pady=20, command=sqrt, bg="#F5CBA7")                   
                   
button_eql= Button(root, text="=", padx=90, pady=20, command=equal, bg="#F1948A")
button_clr= Button(root, text="CLR", padx=85, pady=20, command=clear, bg="#E74C3C")
                   
 
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

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_sqr.grid(row=4, column=1)
button_sqrt.grid(row=4, column=2)
button_eql.grid(row=5, column=2, columnspan=2)
button_clr.grid(row=5, column=0, columnspan=2)

 
root.mainloop()