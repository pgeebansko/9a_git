import tkinter as tk
import func

win = tk.Tk()
win.title(' Суперски проект')
win.geometry('800x600')
win.configure(bg='red')
btn = tk.Button(win, text='Click me!', command=func.my_function)
btn.pack()
win.mainloop()