'''
Created on Dec 8, 2011

@author: pfl
'''

import tkinter as tk

def result():
    print( " this sum of 2+2 is : ", 2+2)
    
    
win = tk.Frame()
win.pack()
label1 = tk.Label( win, text = "click Add to get the sum.").pack(side=tk.TOP)
canvas1= tk.Canvas()
canvas1.pack()

button1 = tk.Button( win, text = "add", command = result, cursor="plus")
button1.pack(side=tk.LEFT)
button2 = tk.Button( win, text = "Quit", command = win.quit)
button2.pack(side=tk.RIGHT)


canvas1.create_line(0,0,50,100,200,200)
canvas1.create_oval(100,100,150,150)

button2.flash()

win.mainloop()