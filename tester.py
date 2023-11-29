from tkinter import *
import random
import time
window = Tk()
window.geometry('700x300')
window.title('Крестики нолики')



nazv = Label(window,text='Крестики нолики', font = ('Times New Roman', 20, 'bold'),fg='Red')
buttons = [Button(window,width=5,height=2,font=('Times New Roman', 24, 'bold'),command= lambda x = i:push(x)) for i in range(9)] 
nazv.place(relx=0.7,rely = 0.3,anchor='center')



def stopgame():
    global gamel
    for item in gamel:
        buttons[item].config(state='disabled')
    
def win(n):
    global game
    if (game[0]== n and game[1]== n and game[2]==n) or (game[3]== n and game[4]== n and game[5]==n) or (game[6]== n and game[7]== n and game[8]==n)\
            or (game[0]== n and game[3]== n and game[6]==n) or (game[1]== n and game[4]== n and game[7]==n) or (game[2]== n and game[5]== n and game[8]==n)\
            or (game[0]== n and game[4]== n and game[8]==n) or (game[2]== n and game[4]== n and game[6]==n):
        return True
turn = 0
game = [None] * 9
gamel= list(range(9))

def push(b):
    global game
    global gamel
    global turn
    game[b]='X'
    buttons[b].config(text='X',state='disabled')
    gamel.remove(b)
    if b ==4 and turn == 0:
        t = random.choice(gamel)
    elif b != 4 and turn == 0:
        t = 4
    if turn > 0:
        t= 8 - b
    if t  not in gamel:
        try:
            t = random.choice(gamel)
        except IndexError:
            nazv['text']='Ничья!'
            stopgame()
    game[t]='O'
    time.sleep(0.5)
    buttons[t].config(text='O',state='disabled')
    if win('X'):
        buttons[t].config(text='',state='disabled')
        nazv['text']='Вы победили!'
        stopgame()
    elif win('O'):
        nazv['text']='Вы проиграли!'
        stopgame()
    else:
        if (len(gamel) > 1):
            gamel.remove(t)
        else:
            nazv['text']='Ничья!'
            stopgame()
        turn += 1

row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row,column=col)
    col += 1
    if col ==3:
        row +=1
        col=0



window.mainloop()












