from tkinter import *
import calendar

text = calendar.calendar(2022)

root=Tk()
root.geometry("530x700")
root.title("CALENDAR")
label1=Label(root, text="CALENDAR", bg="cyan", font=("times",28,"bold"))
label1.grid(row=1, column=1)
root.config(background="cyan")
l1=Label(root, text=text,font="consoles 10 bold")
l1.grid(row=2, column=1, padx=20)
root.mainloop()