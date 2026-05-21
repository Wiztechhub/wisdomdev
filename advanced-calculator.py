from tkinter import *
import tkinter as tk
import math

window=tk.Tk()
window.title("Wiztech Calculator")
window.geometry("255x340")
window.resizable(0,0)

def Button_click(number):
    current=e.get()
    e.delete (0,END)
    e.insert(0, str(current) + str(number))

def btn_add():
    first_num=e.get()
    global f_num
    global math
    math="addition"
    f_num=eval(first_num)
    e.delete(0,END)

#............subtraction function.................
def Btn_sub():
    first_num=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=eval(first_num)
    e.delete(0,END)
    
#..............multiplication function.................
def Btn_multiply():
    first_num=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=eval(first_num)
    e.delete(0,END)
    
#................division function.........................
def Btn_divide():
    first_num=e.get()
    global f_num
    global math
    math="division"
    f_num=eval(first_num)
    e.delete(0,END)
    
def Btn_power():
    first_num=e.get()
    global f_num
    global math
    math="square"
    f_num=eval(first_num)
    e.delete(0,END)

def Btn_dot(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    

def Button_cos(number):
    current=e.get()
    e.insert(0,str(current) + str(number))
    e.delete(0,END)
     
    

def Button_sin():
    return

def Button_tan():
    return

def Button_ln():
    return

def Button_ln():
    return

def Btn_exit():
    window.destroy()
    

def btn_equal():
    second_num=e.get()
    e.delete(0,END)
    if math==" ":
        tk.messagebox.showwarning(title="Error Message!!!", message="Syntax Error")
    if math=="addition":
        e.insert(0,f_num + eval(second_num))
    if math=="subtraction":
        e.insert(0,f_num - eval(second_num))
    if math=="multiplication":
        e.insert(0,f_num *eval(second_num))
    if math=="square":
        e.insert(0, str(f_num*f_num))
    if math=="division":
        e.insert(0,f_num / eval(second_num))
    if math=="cos":
        e.insert(0,eval(math.cos(f_num))) 

def btn_clear():
    e.delete(0,END)
    
  
        
label1=tk.Label(text="view", fg="black")
label1.grid(row=0, column=0, padx=2, pady=2)

label2=tk.Label(text="Edit", fg=r"black")
label2.grid(row=0, column=1, padx=2, pady=2)

label3=tk.Label(text="Help", fg="black")
label3.grid(row=0, column=2, padx=2, pady=2)

copy_right=tk.Label(text="WIZTECH CALCULATOR",fg="purple")
copy_right.grid(row=9,column=1,columnspan=3)

#----------------ENTRY--------------------
e=tk.Entry(window,width="11",font=("algeria",30))
e.grid(row=1, column=0, columnspan=20)


#-----------------BUTTONS-----------------
button1=tk.Button(window,text="sin", width="5",cursor="hand2", command=lambda:Button_sin())
button1.grid(row=2, column=0, padx=2, pady=2)

button2=tk.Button(window,text="cos", width="5",cursor="hand2", command=lambda:Button_cos("COS"))
button2.grid(row=2, column=1, padx=2, pady=2)

button3=tk.Button(window,text="tan", width="5",cursor="hand2", command=lambda:Button_tan())
button3.grid(row=2, column=2, padx=2, pady=2)

button4=tk.Button(window,text="log", width="5",cursor="hand2", command=lambda:Button_log())
button4.grid(row=2, column=3, padx=2, pady=2)

button5=tk.Button(window,text="(", width="5",cursor="hand2", command=lambda:Button_br1())
button5.grid(row=2, column=4, padx=2, pady=2)

button6=tk.Button(window,text=")", width="5",cursor="hand2", command=lambda:Button_br2())
button6.grid(row=3, column=0, padx=2, pady=2)

button7=tk.Button(window,text="ln", width="5",cursor="hand2", command=lambda:Button_ln())
button7.grid(row=3, column=1, padx=2, pady=2)

button8=tk.Button(window,text="EXP", width="5",cursor="hand2", command=lambda:Button_exp())
button8.grid(row=3, column=2, padx=2, pady=2)

button9=tk.Button(window,text="+ ", width="5", cursor="hand2", command=lambda:btn_add())
button9.grid(row=3, column=3, padx=2, pady=2)

button10=tk.Button(window,text="#", width="5",cursor="hand2", command=lambda:Button_click(1))
button10.grid(row=3, column=4,padx=2, pady=2)

button11=tk.Button(window,text="7", width="5",cursor="hand2", command=lambda:Button_click(7))
button11.grid(row=4, column=0, padx=2, pady=2)

button12=tk.Button(window,text="8", width="5",cursor="hand2", command=lambda:Button_click(8))
button12.grid(row=4, column=1, padx=2, pady=2)

button13=tk.Button(window,text="9", width="5",cursor="hand2", command=lambda:Button_click(9))
button13.grid(row=4, column=2, padx=2,)

button14=tk.Button(window,text="/", width="5",cursor="hand2", command=lambda:Btn_divide())
button14.grid(row=4, column=3, padx=2, pady=2)

button15=tk.Button(window,text="%", width="5",cursor="hand2")
button15.grid(row=4, column=4, padx=2, pady=2)

button16=tk.Button(text="4", width="5",cursor="hand2", command=lambda:Button_click(4))
button16.grid(row=5, column=0, padx=2, pady=2)

button17=tk.Button(window,text="5", width="5",cursor="hand2", command=lambda:Button_click(5))
button17.grid(row=5, column=1, padx=2, pady=2)

button18=tk.Button(window,text="6", width="5",cursor="hand2", command=lambda:Button_click(6))
button18.grid(row=5, column=2, padx=2, pady=2)

button19=tk.Button(window,text="*", width="5",cursor="hand2", command=lambda:Btn_multiply())
button19.grid(row=5, column=3, padx=2, pady=2)

button20=tk.Button(window,text="EXIT", width="5",cursor="hand2",command=Btn_exit)
button20.grid(row=5, column=4, padx=2, pady=2)

button21=tk.Button(window,text="1", width="5", cursor="hand2", command=lambda:Button_click(1))
button21.grid(row=6, column=0, padx=2, pady=2)

button22=tk.Button(window,text="2", width="5",cursor="hand2", command=lambda:Button_click(2))
button22.grid(row=6, column=1, padx=2, pady=2)

button23=tk.Button(window,text="3", width="5",cursor="hand2", command=lambda:Button_click(3))
button23.grid(row=6, column=2, padx=2, pady=2)

button24=tk.Button(window,text="-", width="5",cursor="hand2", command=lambda:Btn_sub())
button24.grid(row=6, column=3, padx=2, pady=2)

button25=tk.Button(window,text="=", width="5", height="2",cursor="hand2",command=lambda:btn_equal())
button25.grid(row=6, column=4, padx=2, pady=2)

button26=tk.Button(window,text="0", width="5",cursor="hand2", command=lambda:Button_click(0))
button26.grid(row=7, column=0, padx=2, pady=2)

button27=tk.Button(window,text=".", width="5",cursor="hand2",command=lambda:Btn_dot())
button27.grid(row=7, column=1, padx=2, pady=2)

button28=tk.Button(window,text="square", width="5",cursor="hand2", command=lambda:Btn_power())
button28.grid(row=7, column=2, padx=2, pady=2)

button29=tk.Button(window,text="~", width="5",cursor="hand2")
button29.grid(row=7, column=3, padx=2, pady=2)

button30=tk.Button(window,text="~1", width="5",cursor="hand2")
button30.grid(row=7, column=4, padx=2, pady=2)

button_clear=tk.Button(window,text="CLEAR", width=33,height=2, cursor="hand2", bg="black", fg="white", command=lambda:btn_clear())
button_clear.grid(row=8, column=0, padx=5, pady=5,columnspan=5)                                                                                          




window.mainloop()

