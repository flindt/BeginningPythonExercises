'''
Created on Dec 6, 2012

@author: flindt
'''



import tkinter as tk

def result():
    print( " this sum of 2+2 is : ", 2+2)
    resultVar.set( str(int(resultVar.get())+10) )
    textVar.set("does it work")

    
mainWindow = tk.Tk()
mainWindow.title("testing...")
    
# Create a fraom to hold all the GUI elements
win = tk.Frame()    
    
# StringVar is the connection from the GUI to the code in this file
# Update them with .set in the callback functions  
resultVar = tk.StringVar()
resultVar.set("99")

textVar = tk.StringVar()
textVar.set("starting...")


win.pack()
label1 = tk.Label( win, textvariable=textVar).pack(side=tk.TOP)
button1 = tk.Button( win, text = "add", command = result, cursor="plus").pack(side=tk.LEFT)
button2 = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)
textEntry1 = tk.Entry( win,  textvariable=resultVar).pack(side=tk.BOTTOM)




win.mainloop()