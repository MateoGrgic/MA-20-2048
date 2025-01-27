# Name      : 2048.py
# Author    : Mateo Grgic
# Date      : 20.01.2025

from tkinter import *

number = [[2,4,8,16],
          [32,64,128,512],
          [1024,2048,4096,8162],
          [0,0,0,0]]
'''
number = [[0,0,0,2],
          [0,0,0,0],
          [0,2,0,0],
          [0,0,0,0]]
'''


case = [
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None]
]


window = Tk()
window.title("2048")
window.geometry("800x800")


#Frame
frame_score_reset = Frame(window,bg="black")
frame_score_reset.pack(fill=X)

frame_tableau = LabelFrame(window,bg="black")
frame_tableau.pack(fill=X)

frame_ligne = Frame(frame_tableau,bg="black")
frame_ligne.pack()


#Label
label_score = Label(frame_score_reset,text="Score :",font=("Arial", 25, "bold"),fg="lightblue",bg="black")
label_score.pack(side=LEFT)

for line in range(len(number)):
    for col in range(len(number[line])):
        label_l1_c1 = Label(frame_ligne,text=number[line][col], font=("Arial", 25, "bold"),fg="lightblue", bg="darkblue",borderwidth=50,height=1,width=2)
        label_l1_c1.grid(row=line, column=col,padx=5,pady=5)



#Bouton
btn_reset = Button(frame_score_reset,text="Recommencer",font=("Arial", 25, "bold"),fg="lightblue",bg="black")
btn_reset.pack(side=RIGHT)

window.mainloop()