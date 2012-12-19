'''
Created on Dec 8, 2011

@author: pfl
'''

import tkinter as tk

def result():
    print( " this sum of 2+2 is : ", 2+2)
    

mainWindow = tk.Tk()
mainWindow.title("testing...")

win = tk.Frame()
win.pack()
label1 = tk.Label( win, text = "click Add to get the sum.").pack(side=tk.TOP)
button1 = tk.Button( win, text = "add", command = result, cursor="plus").pack(side=tk.LEFT)
button2 = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)



win.mainloop()