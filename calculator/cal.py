from ast import Global
from tkinter import *
import math

root = Tk()
root.title("calculator")
e= Entry(root, width=45,borderwidth=10)
e.grid(row=0,column=0,columnspan=4)

def click(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
def clean():
    e.delete(0,END)
def adding():
    first_number = e.get()
    global f_num
    global maths
    maths = "add"
    f_num = int(first_number)
    e.delete(0,END)
def result():
    second_number = e.get()
    e.delete(0,END)
    if maths=="add":
         e.insert(0,f_num+int(second_number))
    if maths=="minus":
         e.insert(0,f_num-int(second_number))
    if maths=="multiply":
         e.insert(0,f_num*int(second_number))
    if maths=="divide":
         e.insert(0,f_num/int(second_number))
    if maths=="square root":
        second_number = math.sqrt(f_num)
        e.insert(0,second_number)
def subtracting():
    first_number = e.get()
    global f_num
    global maths
    maths = "minus"
    f_num = int(first_number)
    e.delete(0,END)
def multiplying():
    first_number = e.get()
    global f_num
    global maths
    maths = "multiply"
    f_num = int(first_number)
    e.delete(0,END)
def squaring():
    first_number = e.get()
    global f_num
    global maths
    maths = "square root"
    f_num = int(first_number)
    e.delete(0,END)
def divide():
    first_number = e.get()
    global f_num
    global maths
    maths = "divide"
    f_num = int(first_number)
    e.delete(0,END)
button_1= Button(root,text="1",padx=45,pady=30,fg="black",command=lambda :click(1))
button_2= Button(root,text="2",padx=45,pady=30,fg="black",command=lambda :click(2))
button_3= Button(root,text="3",padx=45,pady=30,fg="black",command=lambda :click(3))
button_4= Button(root,text="4",padx=45,pady=30,fg="black",command=lambda :click(4))
button_5= Button(root,text="5",padx=45,pady=30,fg="black",command=lambda :click(5))
button_6= Button(root,text="6",padx=45,pady=30,fg="black",command=lambda :click(6))
button_7= Button(root,text="7",padx=45,pady=30,fg="black",command=lambda :click(7))
button_8= Button(root,text="8",padx=45,pady=30,fg="black",command=lambda :click(8))
button_9= Button(root,text="9",padx=45,pady=30,fg="black",command=lambda :click(9))
button_0= Button(root,text="0",padx=102,pady=30,fg="black",command=lambda :click(0))
button_add= Button(root,text="+",padx=35,pady=30,fg="black",command=adding)
button_minus= Button(root,text="-",padx=35,pady=30,fg="black",command=subtracting)
button_mltiplication= Button(root,text="*",padx=35,pady=30,fg="black",command=multiplying)
button_equal= Button(root,text="=",padx=35,pady=30,fg="black",command=result)
button_square= Button(root,text="√",padx=45,pady=30,fg="black",command=squaring)
button_clear= Button(root,text="CLEAR",padx=142,fg="black",pady=30,command=clean)
button_divison= Button(root,text="*",padx=35,fg="black",pady=30,command=divide)


button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=0,columnspan=2)
button_square.grid(row=5,column=2)
button_equal.grid(row=5,column=3)
button_add.grid(row=4,column=3)
button_minus.grid(row=3,column=3)
button_mltiplication.grid(row=2,column=3)
button_divison.grid(row=1,column=3)
button_clear.grid(row=1,column=0,columnspan=3)

root.mainloop()
