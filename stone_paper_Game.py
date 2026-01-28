from tkinter import *
screen = Tk()
screen.geometry("500x500")
screen.config(background="#e1bee7")
import random
user_var=StringVar()
user_s = IntVar()
comp_var=StringVar()
comp_score=IntVar()
lbl_var=StringVar()
choices = ["Rock","Paper","Scissor"]
user_var.set("Pending")
comp_var.set("Pending")
user_s.set("0")
comp_score.set("0")
def myfun1():
    comp_var.set(random.choice(choices))
    user_var.set("Rock")
    if user_var.get() == comp_var.get():
        lbl_var.set("Tie Game")
    elif user_var.get() =="Rock" and comp_var.get() == "Paper":
        comp_score.set(comp_score.get()+1)
        lbl_var.set("Computer win")
    elif user_var.get() == "Paper" and comp_var.get() == "Rock":
        user_s.set(user_s.get()+1)
        lbl_var.set("You win")
    elif user_var.get() == "Scissor" and comp_var.get() == "Rock":
        comp_score.set(comp_score.get()+1)
        lbl_var.set("Computer win")
    elif user_var.get() == "Rock" and comp_var.get() == "Scissor":
        user_s.set(user_s.get()+1)
        lbl_var.set("You win")
def myfun2():
    comp_var.set(random.choice(choices))
    user_var.set("Paper")
    if user_var.get() == comp_var.get():
        lbl_var.set("Tie Game")
    elif user_var.get() =="Rock" and comp_var.get() == "Paper":
        comp_score.set(comp_score.get()+1)
        lbl_var.set("Computer win")
    elif user_var.get() == "Paper" and comp_var.get() == "Rock":
        user_s.set(user_s.get()+1)
        lbl_var.set("You win")
    elif user_var.get() == "Paper" and comp_var.get() == "Scissor":
        comp_score.set(comp_score.get()+1)
        lbl_var.set("Computer win")
    elif user_var.get() == "Scissor" and comp_var.get() == "Paper":
        user_s.set(user_s.get()+1)
        lbl_var.set("You win")
def myfun3():
    comp_var.set(random.choice(choices))
    user_var.set("Scissor")
    if user_var.get() == comp_var.get():
        lbl_var.set("Tie Game")
    elif user_var.get() =="Scissor" and comp_var.get() == "Rock":
        comp_score.set(comp_score.get()+1)
        lbl_var.set("Computer win")
    elif user_var.get() == "Rock" and comp_var.get() == "Scissor":
        user_s.set(user_s.get()+1)
        lbl_var.set("You win")
    elif user_var.get() == "Paper" and comp_var.get() == "Scissor":
        comp_score.set(comp_score.get()+1)
        lbl_var.set("Computer win")
    elif user_var.get() == "Scissor" and comp_var.get() == "Paper":
        user_s.set(user_s.get()+1)
        lbl_var.set("You win")
#========================== welcome screen ====================
lbl=Label(screen,text="welcome To Rock paper Scissor Game",font=("arial",14,"bold"),bg="#e1bee7")
lbl.pack()
#=========================== begin : user ======================

btn1 = Button(screen,text="Rock",font=("arial",14,"bold"),height=3,width=7,bd=3,bg="#7986cb",fg="white",command=myfun1)
btn1.place(x=50,y=50)

btn2 = Button(screen,text="Paper",font=("arial",14,"bold"),height=3,width=7,bd=3,bg="#7986cb",fg="white",command=myfun2)
btn2.place(x=200,y=50)

btn3 = Button(screen,text="Scissor",font=("arial",14,"bold"),height=3,width=7,bd=3,bg="#7986cb",fg="white",command=myfun3)
btn3.place(x=350,y=50)

user_label = Label(screen,text="User",font=("arial",14,"bold"),fg="#3f51b5",bg="#e1bee7")
user_label.place(x=50,y=190)

btn4 = Button(screen,text="Pending",textvariable=user_var,font=("arial",10,"bold"),height=2,width=10,bd=3,bg="#3949ab",fg="white")
btn4.place(x=200,y=180)

user_score = Button(screen,text="0",textvariable=user_s,font=("arial",10,"bold"),height=2,width=10,bd=3,bg="white",fg="#ef5350")
user_score.place(x=350,y=180)
#============================ computer ==========================
comp_lbl = Label(screen,text="Computer",font=("arial",14,"bold"),fg="#3f51b5",bg="#e1bee7")
comp_lbl.place(x=50,y=290)

btn5 = Button(screen,text="Pending",textvariable=comp_var,font=("arial",10,"bold"),height=2,width=10,bd=3,bg="#3949ab",fg="white")
btn5.place(x=200,y=280)

computer_score = Button(screen,text="0",textvariable=comp_score,font=("arial",10,"bold"),height=2,width=10,bd=3,bg="white",fg="#ef5350")
computer_score.place(x=350,y=280)
#========================== display =============================
lbl = Label(screen,textvariable=lbl_var,font=("arial",14,"bold"),width=10,bg="#e1bee7",fg="red")
lbl.place(x=200,y=400)
screen.mainloop()