
from tkinter import *
import random
from tkinter import messagebox

# Fonction pour afficher le jeu
def display_game():
    for line in range(len(case)):
        for col in range(len(case[line])):
            case[line][col].config(
                text=number[line][col] or "",
                bg=color[number[line][col]]
            )
    return



already_win = False

def win_game():
    global already_win
    if already_win == True:
        return False
    for col in number:
        for line  in col:
            if  line   == 2048:
                messagebox.showinfo("Victoire !", "Félicitations ! Vous avez atteint 2048 🎉")
                already_win = True  # On marque la victoire pour ne pas répéter l'affichage
                return True
    return False  # Aucun 2048 trouvé

def is_game_full():
    for line in range(len(number)):
        for col in range(len(number[line])):
            if number[line][col] == 0:

                return False
    return True

def count_mergeable():
    count = 0
    for line in range(len(number)):
        for col in range(len(number[line]) - 1):
            if number[line][col] == number[line][col + 1]:
                count += 1
    for col in range(len(number[0])):
        for line in range(len(number) - 1):
            if number[line][col] == number[line + 1][col]:
                count += 1
    return count


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


def spawn_tile(): #ChatGPT
    # Trouver toutes les cases vides
    empty_positions = [(i, j) for i in range(4) for j in range(4) if number[i][j] == 0]

    if empty_positions:
        i, j = random.choice(empty_positions)  # Choisir une position vide aléatoire
        number[i][j] = random.choice([2, 4])  # Ajouter un 2 ou un 4 (90% de chance d'obtenir un 2)
        display_game()  # Mettre à jour l'affichage

def move_and_spawn(move_function, event): #ChatGPT
    old_number = [row[:] for row in number]  # Sauvegarde du plateau

    move_function(event)  # Applique le mouvement

    if old_number != number:  # Vérifie si un mouvement a eu lieu
        spawn_tile()  # Ajoute une nouvelle tuile
        win_game()
        if is_game_full() and count_mergeable() == 0:
            messagebox.showinfo("defaite","Tableau rempli")
        display_game()  # Met à jour l'affichage


# Fonction pour déplacer toutes les lignes vers la gauche
def tasse_left(event): #ChatGPT
    move_and_spawn(_tasse_left, event)

def tasse_right(event): #ChatGPT
    move_and_spawn(_tasse_right, event)

def tasse_up(event): #ChatGPT
    move_and_spawn(_tasse_up, event)

def tasse_down(event): #ChatGPT
    move_and_spawn(_tasse_down, event)

# Déplacer l'ancienne logique des mouvements dans des fonctions internes
def _tasse_left(event):
    for li in range(len(number)):
        number[li][0], number[li][1], number[li][2], number[li][3], _ = pack_4(
            number[li][0], number[li][1], number[li][2], number[li][3]
        )
    display_game()

def _tasse_right(event):
    for li in range(len(number)):
        number[li][3], number[li][2], number[li][1], number[li][0], _ = pack_4(
            number[li][3], number[li][2], number[li][1], number[li][0]
        )
    display_game()

def _tasse_up(event):
    for col in range(len(number[0])):
        number[0][col], number[1][col], number[2][col], number[3][col], _ = pack_4(
            number[0][col], number[1][col], number[2][col], number[3][col]
        )
    display_game()

def _tasse_down(event):
    for col in range(len(number[0])):
        number[3][col], number[2][col], number[1][col], number[0][col], _ = pack_4(
            number[3][col], number[2][col], number[1][col], number[0][col]
        )
    display_game()




def restart():
    global number, already_win
    already_win = False
    number = [[2, 0, 0, 2],
              [0, 0, 0, 0],
              [0, 2, 2, 0],
              [0, 0, 0, 0]]
    display_game()

# Initialisation du tableau de jeu
number = [[2, 0, 0, 2],
         [0, 0, 0, 0],
         [0, 2, 2, 0],
         [0, 0, 0, 0]]

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