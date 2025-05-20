from tkinter import*
import tkinter.font as font
import random

playerscore=0
botscore=0
options= [("rock",0),("paper",1),("scissor",2)]
def playerchoice(playerinput):
    global playerscore,botscore
    botinput=getbotchoice()
    playerchoicelabel.config(text="your selected:"+playerinput[0])
    botchoicelabel.config(text="bot selected:"+botinput[0])
    if (playerinput==botinput):
        winnerlabel.config(text="tie!")
    elif ((playerinput[1]-botinput[1])%3 ==1):
        playerscore+=1
        winnerlabel.config(text="you won!!!")
        playerscorelabel.config(text="your score:" + str(playerscore))
    else:
        botscore+=1
        winnerlabel.config(text="bot won!!!")
        botscorelabel.config(text="bot score:"+str(botscore))
def getbotchoice():
    return random.choice(options)

gamewindow=Tk()
gamewindow.title("ROCK PAPER SCISSORS GAME")
appfont=font.Font(size=12)

gametitle=Label(text="ROCK PAPER SCISSOR",font=font.Font(size=20),fg="grey")
winnerlabel=Label(text="lets start the game..",fg="green",font=font.Font(size=13),pady=8)
winnerlabel.pack()

inputframe=Frame(gamewindow)
inputframe.pack()

playeroptions=Label(inputframe,text="your options:",font=appfont,fg="grey")
playeroptions.grid(row=0,column=0,pady=8)

rockbtn=Button(inputframe,text="Rock",width=15,bd=0,bg="pink",pady=5,command=lambda:playerchoice(options[0]))
rockbtn.grid(row=1,column=1,padx=8,pady=5)

paperbtn=Button(inputframe,text="Paper",width=15,bd=0,bg="silver",pady=5,command=lambda:playerchoice(options[1]))
paperbtn.grid(row=1,column=2,padx=8,pady=5)

scissorbtn=Button(inputframe,text="scissors",width=15,bd=0,bg="light blue",pady=5,command=lambda:playerchoice(options[2]))
scissorbtn.grid(row=1,column=3,padx=8,pady=5)

scorelabel=Label(inputframe,text="score:",font=appfont,fg="grey")
scorelabel.grid(row=2,column=0)

playerchoicelabel=Label(inputframe,text="your selected:",font=appfont)
playerchoicelabel.grid(row=3,column=1,pady=5)

playerscorelabel=Label(inputframe,text="your score:",font=appfont)
playerscorelabel.grid(row=3,column=2,pady=5)

botchoicelabel=Label(inputframe,text="bot selected:",font=appfont,fg="black")
botchoicelabel.grid(row=4,column=1,pady=5)

botscorelabel=Label(inputframe,text="bot score:",font=appfont,fg="black")
botscorelabel.grid(row=4,column=2,padx=(10,0),pady=5)

gamewindow.geometry("700x300")
gamewindow.mainloop()
