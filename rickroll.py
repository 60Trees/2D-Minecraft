from tkinter import *

def make_another():
 launch_window()

def launch_window():
 root = Tk()
 l = Label(root, text='IMAGINE GETTING RICKROLLED!!!!!')
 l.pack()
 root.protocol("WM_DELETE_WINDOW", make_another)
 root.mainloop()

launch_window()