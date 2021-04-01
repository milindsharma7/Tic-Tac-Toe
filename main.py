from tkinter import *
from tkinter import messagebox

root =Tk()
root.title('Tic-Tac-Toe')
flag=True
count=0

def button_click(b):
    global flag 
    global count
    if b["text"]==" " and flag==True:
        b["text"]="X"
        player_win()
        flag=False
        count=count+1
    elif b["text"]==" " and flag==False:
        b["text"]="O"
        flag=True
        count=count+1
def player_win():
    global flag2
    if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X":
        button1.config(bg="indian red")
        button2.config(bg="indian red")
        button3.config(bg="indian red")
        messagebox.showinfo("First Player won the game")
                
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
