from tkinter import *
from tkinter.ttk import *
from time import *
import os

def update_time():

     #add day of the week
    day_str= strftime("%A")
    day_label.config(text= day_str)

    #add clock
    time_str= strftime('%I:%M:%S %p')
    time_label.config(text= time_str)
    #update every 1 second with recursion
    window.after(1000, update_time)



window = Tk()
day_label= Label(window, font= ("cambria", 70), foreground= "pink", background= "black")
day_label.pack()

time_label= Label(window, font= ("cambria", 50), foreground= "cyan", background= "black")
time_label.pack()



update_time()

window.mainloop()
