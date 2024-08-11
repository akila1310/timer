import datetime
from logging import root
from pyclbr import Class
from re import T, X
import tkinter as tk
from tkinter import BOTTOM, LEFT, NO, TOP, Button, Entry, Frame, Label, StringVar, ttk
from tkinter import messagebox
import time
import sys
import tkinter
from turtle import update
from typing_extensions import IntVar





def  count():

      
      extra_window =tk.Toplevel()
      extra_window.title('countdown ')
      extra_window.geometry('800x800')
      extra_window.config(bg="#000")
      extra_window.resizable(False,False)
    

      title = tk.Label(extra_window,text="CountDown Timer",font=("Arial",24),fg="purple")
      title.pack(pady=60,padx=60)

      

      hour = StringVar()
      minute = StringVar()
      second = StringVar()
      hour.set("00")
      minute.set("00")
      second.set("00")

      hourEntry = Entry(extra_window, width=2, font=("Arial", 50, ""), textvariable=hour,fg="red")
      hourEntry.place(x=200, y=300)
      minuteEntry = Entry(extra_window, width=2, font=("Arial", 50, ""), textvariable=minute,fg="red")
      minuteEntry.place(x=370, y=300)
      secondEntry = Entry(extra_window, width=2, font=("Arial", 50, ""), textvariable=second,fg="red")
      secondEntry.place(x=540, y=300)
      label1 = tk.Label(extra_window,text="Hour",font=("Arial",24),bg="black",fg="purple")
      label1.place(x=280,y=330)
      label2 = tk.Label(extra_window,text="Mins",font=("Arial",24),bg="black",fg="purple")
      label2.place(x=450,y=330)
      label3 = tk.Label(extra_window,text="Secs",font=("Arial",24),bg="black",fg="purple")
      label3.place(x=620,y=330)
      

      def submit():
          try:
             temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
          except ValueError:
             print("Please input the right value")

          while temp > -1:
              mins, secs = divmod(temp, 60)
              hours = 0
              if mins > 60:
                hours, mins = divmod(mins, 60)
              

              hour.set("{0:02d}".format(hours))
              minute.set("{0:02d}".format(mins))
              second.set("{0:02d}".format(secs)) 
              extra_window.update()
              time.sleep(1)
          
              if(temp==0):  
                 messagebox.showinfo("Time Countdown", "Time's up!")
              temp -= 1      

      btn = Button(extra_window, text="Set Time Countdown", bd=5, command=submit,font=("Arial",20),bg="cyan",border=5 )
      btn.place(x=290, y=500)

      extra_window.mainloop()
     
      

      extra_window.mainloop()
    

window =tk.Tk()
window.geometry('500x500')
window.title('Multiple window')
button1= tk.Button(window,text='COUNTDOWN',command=count,font=("Arial",19,"bold"),bg="purple")
button1.pack(expand=True)










       
window.mainloop()
