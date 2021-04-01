from tkinter.constants import DISABLED
import main
from tkinter import messagebox

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
        if count==9:
            disable()
            messagebox.showinfo(title="Tic-Tac-Toe",message="This game is a draw")
            
    elif b["text"]==" " and flag==False:
        b["text"]="O"
        flag=True
        player_win()
        count=count+1
        if count==9:
            disable()
            messagebox.showinfo(title="Tic-Tac-Toe",message="This game is a draw")

def disable():
    main.button1.config(state=DISABLED)
    main.button2.config(state=DISABLED)
    main.button3.config(state=DISABLED)
    main.button4.config(state=DISABLED)
    main.button5.config(state=DISABLED)
    main.button6.config(state=DISABLED)
    main.button7.config(state=DISABLED)
    main.button8.config(state=DISABLED)
    main.button9.config(state=DISABLED)


def player_win():
    global count
    if main.button1["text"]=="X" and main.button2["text"]=="X" and main.button3["text"]=="X":
        main.button1.config(bg="indian red")
        main.button2.config(bg="indian red")
        main.button3.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button4["text"]=="X" and main.button5["text"]=="X" and main.button6["text"]=="X":
        main.button4.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button6.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button7["text"]=="X" and main.button8["text"]=="X" and main.button9["text"]=="X":
        main.button7.config(bg="indian red")
        main.button8.config(bg="indian red")
        main.button9.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button1["text"]=="X" and main.button4["text"]=="X" and main.button7["text"]=="X":
        main.button1.config(bg="indian red")
        main.button4.config(bg="indian red")
        main.button7.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button2["text"]=="X" and main.button5["text"]=="X" and main.button8["text"]=="X":
        main.button2.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button8.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button3["text"]=="X" and main.button6["text"]=="X" and main.button9["text"]=="X":
        main.button3.config(bg="indian red")
        main.button6.config(bg="indian red")
        main.button9.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button1["text"]=="X" and main.button5["text"]=="X" and main.button9["text"]=="X":
        main.button1.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button9.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button3["text"]=="X" and main.button5["text"]=="X" and main.button7["text"]=="X":
        main.button3.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button7.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="First Player won the game")
    elif main.button1["text"]=="O" and main.button2["text"]=="O" and main.button3["text"]=="O":
        main.button1.config(bg="indian red")
        main.button2.config(bg="indian red")
        main.button3.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")
    elif main.button4["text"]=="O" and main.button5["text"]=="O" and main.button6["text"]=="O":
        main.button4.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button6.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")
    elif main.button7["text"]=="O" and main.button8["text"]=="O" and main.button9["text"]=="O":
        main.button7.config(bg="indian red")
        main.button8.config(bg="indian red")
        main.button9.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")
    elif main.button1["text"]=="O" and main.button4["text"]=="O" and main.button7["text"]=="O":
        main.button1.config(bg="indian red")
        main.button4.config(bg="indian red")
        main.button7.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")
    elif main.button2["text"]=="O" and main.button5["text"]=="O" and main.button8["text"]=="O":
        main.button2.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button8.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")
    elif main.button3["text"]=="O" and main.button6["text"]=="O" and main.button9["text"]=="O":
        main.button3.config(bg="indian red")
        main.button6.config(bg="indian red")
        main.button9.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")
    elif main.button1["text"]=="O" and main.button5["text"]=="O" and main.button9["text"]=="O":
        main.button1.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button9.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")
    elif main.button3["text"]=="O" and main.button5["text"]=="O" and main.button7["text"]=="O":
        main.button3.config(bg="indian red")
        main.button5.config(bg="indian red")
        main.button7.config(bg="indian red")
        disable()
        count=0
        messagebox.showinfo(title="Tic-Tac-Toe",message="Second Player won the game")