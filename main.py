from tkinter import *
from tkinter import messagebox

root =Tk()
clicked=True
count=0
def button_click(b):
    pass

button1= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button1))
button2= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button2))
button3= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button3))

button4= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button4))
button5= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button5))
button6= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button6))

button7= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button7))
button8= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button8))
button9= Button(root,text=" ",font=("Helvetica",25),height =2,width=5,bg="Light Blue",command=lambda:button_click(button9))

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

root.mainloop()
