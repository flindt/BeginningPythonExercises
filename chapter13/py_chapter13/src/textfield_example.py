'''
Created on Dec 6, 2012

@author: flindt
'''



import tkinter as tk

def result():
    print( " this sum of 2+2 is : ", 2+2)
    resultVar.set( 2+2 )
    
    
    
    
win = tk.Frame()    
    
resultVar = tk.StringVar()
resultVar.set("trying...")


win.pack()
label1 = tk.Label( win, text = "click Add to get the sum.").pack(side=tk.TOP)
button1 = tk.Button( win, text = "add", command = result, cursor="plus").pack(side=tk.LEFT)
button2 = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)
textEntry1 = tk.Entry( win,  textvariable=resultVar).pack(side=tk.BOTTOM)




win.mainloop()