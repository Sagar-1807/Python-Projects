from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("CLOCK")

def time():
    string=strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000,time)      # 1sec=1000

lable=Label(root,font=("ds-digital",150),background="black",foreground="yellow")
lable.pack(anchor='center')
time()
mainloop()

