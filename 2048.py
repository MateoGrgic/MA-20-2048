from tkinter import *

# Fonction pour afficher le jeu
def display_game():
    for line in range(len(case)):
        for col in range(len(case[line])):
            case[line][col].config(
                text=number[line][col] or "",
                bg=color[number[line][col]]
            )
    return

# Fonction pour déplacer et fusionner les nombres dans une ligne
def pack_4(d, e, f, g):
    move = 0  # Compteur de déplacements

    # Supprime les zéros et décale les nombres vers la gauche
    if f == 0 and g > 0:
        f = g
        g = 0
    if e == 0 and f > 0:
        e = f
        f = g
        g = 0
        move += 1
    if d == 0 and e > 0:
        d = e
        e = f
        f = g
        g = 0
        move += 1

    # Fusion des nombres adjacents
    if d == e and d > 0:
        d = d * 2
        e = f
        f = g
        g = 0
        move += 1
    if e == f and e > 0:
        e = e * 2
        f = g
        g = 0
        move += 1
    if f == g and f > 0:
        f = f * 2
        g = 0
        move += 1

    return [d, e, f, g, move]



# Fonction pour déplacer toutes les lignes vers la gauche
def tasse_left(event):
    global col
    for li in range(len(number)):
        [number[li][0], number[li][1], number[li][2], number[li][3], n] = pack_4(
            number[li][0], number[li][1], number[li][2], number[li][3])
    display_game()

def tasse_right(event):
    global col
    for li in range(len(number)):
        [number[li][3], number[li][2], number[li][1], number[li][0], n] = pack_4(
             number[li][3], number[li][2], number[li][1], number[li][0])
    display_game()


def tasse_up(event):
    global col
    for col in range(len(number[0])):
        [number[0][col], number[1][col], number[2][col], number[3][col], n] = pack_4(
            number[0][col], number[1][col], number[2][col], number[3][col])
    display_game()


def tasse_down(event):
    global col
    for col in range(len(number[0])):
        [number[3][col], number[2][col], number[1][col], number[0][col], n] = pack_4(
            number[3][col], number[2][col], number[1][col], number[0][col])
    display_game()

def restart():
    global number
    number = [[2, 0, 0, 2],
              [0, 0, 0, 0],
              [0, 2, 2, 0],
              [0, 0, 0, 0]]
    display_game()

# Initialisation du tableau de jeu
number = [[2, 2, 4, 2],
          [2, 2, 0, 2],
          [2, 2, 0, 2],
          [2, 2, 2, 2]]

# Couleurs associées aux nombres
color = {
    0: "white",
    2: "#CC0000",
    4: "#FF0000",
    8: "#FF6666",
    16: "#FF9999",
    32: "#FF8000",
    64: "#FF9933",
    128: "#FFB366",
    256: "#FFCC99",
    512: "#FFFF00",
    1024: "#FFFF66",
    2048: "#FFFF66",
    4096: "#FFB3B3",
    8162: "#FF9999"
}

# Création de la fenêtre principale
window = Tk()
window.title("2048")
window.geometry("600x600")
window.config(bg="black")

# Frame pour le score et le bouton "Recommencer"
frame_score_reset = Frame(window, bg="black")
frame_score_reset.pack(fill=X)

# Frame pour le tableau de jeu
frame_tableau = LabelFrame(window, bg="black")
frame_tableau.pack()

# Label pour afficher le score
label_score = Label(frame_score_reset, text="Score :", font=("Arial", 25, "bold"), fg="white", bg="black")
label_score.pack(side=LEFT)

# Bouton "Recommencer"
btn_reset = Button(frame_score_reset, text="Recommencer", font=("Arial", 25, "bold"), fg="white", bg="black",command=restart)
btn_reset.pack(side=RIGHT)

# Création des cases du tableau
case = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]
]

for line in range(len(number)):
    for col in range(len(number[line])):
        label = Label(
            frame_tableau ,
            text=number[line][col] or "",
            font=("Arial", 25, "bold"),
            fg="black",
            bg=color[number[line][col]],
            borderwidth=1,
            height=3,
            width=6
        )
        label.grid(row=line, column=col, padx=5, pady=5)
        case[line][col] = label   # Enregistrer le label dans la grille des cases

# Liaison de la touche gauche à la fonction tasse_left
window.bind("<Left>", tasse_left)
window.bind("<Right>", tasse_right)
window.bind("<Up>", tasse_up)
window.bind("<Down>", tasse_down)

# Affichage de la fenêtre
window.mainloop()