# Python Digital clock BY Muhammad Nasser

from tkinter import*
import time 

root = Tk()
root.title('Digital Clock')
root.geometry('600x400')

def myTime():
    myText = time.strftime("%I:%M:%S %p")
    myText2 = time.strftime("%A %D ")
    myLabel.config(text=myText)
    myLabel2.config(text=myText2)
    myLabel.after(1000, myTime)
    
myLabel = Label(root, text='\n ', font=('Arial', 72), fg='white', bg='black')
myLabel.pack()
myLabel2 = Label(root, text='\n ', font=('Arial', 48), fg='white', bg='black')
myLabel2.pack()
myLabel3 = Label(root, text='\n BY Muhammad Nasser', font=('Arial', 32), fg='black', bg='white')
myLabel3.pack()

myTime()
root.mainloop()

