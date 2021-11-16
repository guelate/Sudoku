import pygame
import tkinter as tk
from tkinter import * 
pygame.font.init()
pygame.mixer.init()

# Vérifie si les lignes ne contienne pas 0 

def vide(tab):
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if tab[x][y] == 0:
                return (x, y)  
    return None


# vérifie les conditions d'entrée dans la grille 

def scan(tab, valeur, position):

    for x in range(len(tab[0])):
        if tab[position[0]][x] == valeur and position[1] != x:
            return False

    
    for x in range(len(tab)):
        if tab[x][position[1]] == valeur and position[0] != x:
            return False

    
    scan_ligne = (position[1] // 3) * 3
    scan_colonne = (position[0] // 3) * 3

    for x in range(scan_colonne, scan_colonne + 3):
        for y in range(scan_ligne, scan_ligne + 3):
            if tab[x][y] == valeur and (x,y) != position:
                return False

    return True


# Résout la grille 

def resolution(tab):
    scanner = vide(tab)
    if not scanner:
        return True
    else:
        ligne, colonne = scanner

    for x in range(1,10):
        if scan(tab, x, (ligne, colonne)):
            tab[ligne][colonne] = x

            if resolution(tab):
                return True

            tab[ligne][colonne] = 0

    return False

# appel de class --> construction grille 

def construction1(tab):
    tab.dessin()

def construction2(tab):
    tab.dessin1()

def construction3(tab):
    tab.dessin2()


# fenêttre défaite 

def menu1():
    
    root = tk.Tk()
    root["bg"] = "#BDC3C7"  
    root.geometry(f'{500}x{500}+{350}+{90}')
    text = Label(root, text ="  VOUS AVEZ PERDU !", bg = "#EE0808")
    text.place( y = 210, x = 180)

# fenêtre victoire 

def menu2():
    
    root = tk.Tk()
    root["bg"] = "#BDC3C7"  
    root.geometry(f'{500}x{500}+{350}+{90}')
    text = Label(root, text ="  VOUS AVEZ GAGNER !", bg = "#0EF314")
    text.place( y = 210, x = 180)
























