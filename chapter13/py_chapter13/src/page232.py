'''
Created on Dec 8, 2011

@author: pfl
'''


import tkinter as tk

def result():
    print( " this sum of 2+2 is : ", 2+2)
    
    
win = tk.Frame()
win.pack()
tk.Label( win, text = "click Add to get the sum.").pack(side=tk.TOP)
tk.Button( win, text = "add", command = result).pack(side=tk.LEFT)
tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)


win.mainloop()