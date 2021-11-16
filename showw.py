import tkinter as tk
from tkinter import * 
from tkinter import ttk
from load import scan , resolution, construction1 , construction2 , construction3 , menu1 , menu2 
from array import *
import pygame
import time
import random

pygame.mixer.init()
pygame.font.init()


touche = None
fautes = 0
enregistre = (0,0)
chargement = True


#Construction de la grille .

class Jeux():

   
    grille_81 =  [

        [0, 0, 0,      0, 0, 0,          0, 0, 0],
        [0, 0, 0,    0, random.randint(3,4), 0,   random.randint(1,2), 0, 0],
        [0, 0, random.randint(8,9),  0, 0 , 0,   0 , 0 , 0],


        [random.randint(1,2), 0, 0,      0, 0, random.randint(4,5), 0, random.randint(8,9),0],
        [0, 0, 0,      random.randint(6,7), 0, 0,  0, 0 , 0],
        [0, 0, 0,   0, 0, 0,          0, 0, 0],

        
        [0, 0, 0,      0, 0, 0,          0, 0, random.randint(3,4)],
        [random.randint(5,6), 0, 0,      0,0, random.randint(1,2),  0, 0, 0],
        [0, 0, 0,      0, 0, 0,          0, 0, 0]


    ]


    grille1_81 = [
    
        [0, 0, 0,      0, 0, 0,          0, 0, 0],
        [0, 0, 0,    0, random.randint(6,7), 0,   random.randint(4,5), 0, 0],
        [0, 0, random.randint(1,2),  0, 0 , 0,   0 , 0 , 0],


        [random.randint(4,5), 0, 0,      0, 0, random.randint(1,2), 0, random.randint(3,4),0],
        [0, 0, 0,      random.randint(7,8), 0, 0,  0, 0 , 0],
        [0, 0, 0,   0, 0, 0,          0, 0, 0],

        
        [0, 0, 0,      0, 0, 0,          0, 0, random.randint(1,2)],
        [random.randint(8,9), 0, 0,      0,0, random.randint(3,4),  0, 0, 0],
        [0, 0, 0,      0, 0, 0,          0, 0, 0]

    ]



    grille2_81 = [

        [0, 0, 0,      0, 0, 0,          0, 0, 0],
        [0, 0, 0,    0, random.randint(1,2), 0,   random.randint(8,9), 0, 0],
        [0, 0, random.randint(3,4),  0, 0 , 0,   0 , 0 , 0],


        [random.randint(7,8), 0, 0,      0, 0, random.randint(5,6), 0, random.randint(3,4),0],
        [0, 0, 0,      random.randint(1,2), 0, 0,  0, 0 , 0],
        [0, 0, 0,   0, 0, 0,          0, 0, 0],

        
        [0, 0, 0,      0, 0, 0,          0, 0, random.randint(1,2)],
        [random.randint(5,6), 0, 0,      0,0, random.randint(8,9),  0, 0, 0],
        [0, 0, 0,      0, 0, 0,          0, 0, 0]


    ]




    def __init__(self,element,element1, lignes , colonnes ,largeur,hauteur):

        self.fenêtre = element
        self.canvas = element1
        self.canvas.pack()
        self.lignes = lignes
        self.colonnes = colonnes
        self.hauteur = hauteur
        self.largeur = largeur
        self.etat = None
        self.cible = None
        self.carre = [[Remplissage(self.grille_81[x][y], x , y , largeur, hauteur,element1) for y in range(colonnes)] for x in range(lignes)]
        self.carre1 = [[Remplissage(self.grille1_81[x][y], x , y , largeur, hauteur,element1) for y in range(colonnes)] for x in range(lignes)]
        self.carre2 = [[Remplissage(self.grille2_81[x][y], x , y , largeur, hauteur,element1) for y in range(colonnes)] for x in range(lignes)]

    def dessin(self):
        global fautes
        label = Label(self.fenêtre, text = str(fautes) + "/7 FAUTES !!" , fg = "red", bg = "black")
        label.place(y = 555, x = 460)
        btn = Button(self.fenêtre, text = ' Quitter !', width = 10 , bd = 0 , fg = "White", bg = "black" , command = lambda: self.fenêtre.destroy())
        btn.place(y = 560 , x = 0)

        ecart = self.largeur / 9 
        for x in range(self.lignes+1):
            if x % 3 == 0 and x != 0:
                epaisseur = 5 
            else:
                epaisseur = 1

            ligne = self.canvas.create_line(0,x*ecart,540,x*ecart , width = epaisseur)
            ligne = self.canvas.create_line(x*ecart,0,x*ecart,540 , width = epaisseur)
            

        for x in range(self.lignes):
            for y in range(self.colonnes):
                self.carre[x][y].dessin1()
             
        self.fenêtre.mainloop()

    
    def dessin1(self):
        global fautes
        label = Label(self.fenêtre, text = str(fautes) + "/5 FAUTES !!" , fg = "red", bg = "black")
        label.place(y = 555, x = 460)
        btn = Button(self.fenêtre, text = ' Quitter !', width = 10 , bd = 0 , fg = "White", bg = "black" , command = lambda: self.fenêtre.destroy())
        btn.place(y = 560 , x = 0)

        ecart = self.largeur / 9 
        for x in range(self.lignes+1):
            if x % 3 == 0 and x != 0:
                epaisseur = 5 
            else:
                epaisseur = 1

            ligne = self.canvas.create_line(0,x*ecart,540,x*ecart , width = epaisseur)
            ligne = self.canvas.create_line(x*ecart,0,x*ecart,540 , width = epaisseur)
            

        for x in range(self.lignes):
            for y in range(self.colonnes):
                self.carre1[x][y].dessin2()
             
        self.fenêtre.mainloop()

    
    def dessin2(self):
        global fautes
        label = Label(self.fenêtre, text = str(fautes) + "/3 FAUTES !!" , fg = "red", bg = "black")
        label.place(y = 555, x = 460)
        btn = Button(self.fenêtre, text = ' Quitter !', width = 10 , bd = 0 , fg = "White", bg = "black" , command = lambda: self.fenêtre.destroy())
        btn.place(y = 560 , x = 0)

        ecart = self.largeur / 9 
        for x in range(self.lignes+1):
            if x % 3 == 0 and x != 0:
                epaisseur = 5 
            else:
                epaisseur = 1

            ligne = self.canvas.create_line(0,x*ecart,540,x*ecart , width = epaisseur)
            ligne = self.canvas.create_line(x*ecart,0,x*ecart,540 , width = epaisseur)
            

        for x in range(self.lignes):
            for y in range(self.colonnes):
                self.carre2[x][y].dessin3()
             
        self.fenêtre.mainloop()

        
    def localisation(self,coordonnée):

        if coordonnée[0] < self.largeur and coordonnée[1] < self.hauteur:
           
            ecart = self.largeur / 9 
            a = coordonnée[0] // ecart  
            b = coordonnée[1] // ecart 
            return (int(b) , int(a))
        else:
            return None



    def cible1(self, ligne, colonne):
        for x in range(self.lignes):
            for y in range(self.colonnes):
                self.carre[x][y].cible = False

        self.carre[ligne][colonne].cible = True
        self.cible = (ligne, colonne)



    def cible2(self, ligne, colonne):
        for x in range(self.lignes):
            for y in range(self.colonnes):
                self.carre1[x][y].cible = False

        self.carre1[ligne][colonne].cible = True
        self.cible = (ligne, colonne)


    def cible3(self, ligne, colonne):
        for x in range(self.lignes):
            for y in range(self.colonnes):
                self.carre2[x][y].cible = False

        self.carre2[ligne][colonne].cible = True
        self.cible = (ligne, colonne)


    def efface1(self):
        ligne , colonne = self.cible
        if self.carre[ligne][colonne].valeur == 0:
            self.carre[ligne][colonne].ajt_zero(0)

    def efface2(self):
        ligne , colonne = self.cible
        if self.carre1[ligne][colonne].valeur == 0:
            self.carre1[ligne][colonne].ajt_zero(0)

    def efface3(self):
        ligne , colonne = self.cible
        if self.carre2[ligne][colonne].valeur == 0:
            self.carre2[ligne][colonne].ajt_zero(0)

    def ajoute1(self,valeur):
        ligne , colonne = self.cible
        self.carre[ligne][colonne].ajt_zero(valeur)

    def ajoute2(self,valeur):
        ligne , colonne = self.cible
        self.carre1[ligne][colonne].ajt_zero(valeur)

    def ajoute3(self,valeur):
        ligne , colonne = self.cible
        self.carre2[ligne][colonne].ajt_zero(valeur)


    def insere1(self,valeur):
        ligne,colonne = self.cible
        if self.carre[ligne][colonne].valeur == 0:
            self.carre[ligne][colonne].set(valeur)
            self.actualise1()
            
            if scan(self.etat, valeur , (ligne ,colonne)) and resolution(self.etat):
                
                return True
            
            else:
                
                self.carre[ligne][colonne].set(0)
                self.carre[ligne][colonne].ajt_zero(0)
                self.actualise1()
                return False 


    def insere2(self,valeur):
        ligne,colonne = self.cible
        if self.carre1[ligne][colonne].valeur == 0:
            self.carre1[ligne][colonne].set(valeur)
            self.actualise2()
            
            if scan(self.etat, valeur , (ligne ,colonne)) and resolution(self.etat):
                
                return True
            
            else:
                
                self.carre1[ligne][colonne].set(0)
                self.carre1[ligne][colonne].ajt_zero(0)
                self.actualise2()
                return False 


    def insere3(self,valeur):
        ligne,colonne = self.cible
        if self.carre2[ligne][colonne].valeur == 0:
            self.carre2[ligne][colonne].set(valeur)
            self.actualise3()
            
            if scan(self.etat, valeur , (ligne ,colonne)) and resolution(self.etat):
                
                return True
            
            else:
                
                self.carre2[ligne][colonne].set(0)
                self.carre2[ligne][colonne].ajt_zero(0)
                self.actualise3()
                return False 

    
        
    def actualise1(self):
        self.etat = [[self.carre[x][y].valeur for y in range(self.colonnes)] for x in range(self.lignes)]
        
    def actualise2(self):
        self.etat = [[self.carre1[x][y].valeur for y in range(self.colonnes)] for x in range(self.lignes)]
        
        
    def actualise3(self):
        self.etat = [[self.carre2[x][y].valeur for y in range(self.colonnes)] for x in range(self.lignes)]
        
        
    def ferme(self):
        self.fenêtre.destroy()
        
    def terminer1(self):
        for x in range(self.lignes):
            for y in range(self.colonnes):
                if self.carre[x][y].valeur == 0:
                    return False
            return True


    def terminer2(self):
        for x in range(self.lignes):
            for y in range(self.colonnes):
                if self.carre1[x][y].valeur == 0:
                    return False
        return True


    def terminer3(self):
        for x in range(self.lignes):
            for y in range(self.colonnes):
                if self.carre2[x][y].valeur == 0:
                    return False
        return True

# Remplissage de la grille : ajoute de chiffre dans la grille , supression de chiffre .


class Remplissage():
    lignes = 9
    colonnes = 9

    def __init__(self,valeur,ligne,colonne,largeur,hauteur,element1):
        self.canvas = element1
        self.valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self.largeur = largeur
        self.hauteur = hauteur
        self.cible = False
        self.entrer = 0

    def dessin1(self):
        
        ecart = self.largeur / 9 
        x = self.colonne * ecart
        y = self.ligne * ecart

        if self.entrer != 0 and self.valeur == 0:
            None
        elif not(self.valeur == 0):
            chiffre = self.canvas.create_text( ((ecart/2) + x), ((ecart/2) + y) , text = self.valeur, font = 1)


    def dessin2(self):
        
        ecart = self.largeur / 9 
        x = self.colonne * ecart
        y = self.ligne * ecart

        if self.entrer != 0 and self.valeur == 0:
            None
        elif not(self.valeur == 0):
            chiffre = self.canvas.create_text( ((ecart/2) + x), ((ecart/2) + y) , text = self.valeur, font = 1)
    
    def dessin3(self):
        
        ecart = self.largeur / 9 
        x = self.colonne * ecart
        y = self.ligne * ecart

        if self.entrer != 0 and self.valeur == 0:
            None
        elif not(self.valeur == 0):
            chiffre = self.canvas.create_text( ((ecart/2) + x), ((ecart/2) + y) , text = self.valeur, font = 1)
        


    def ajt_zero(self, valeur):
        self.entrer = valeur

    def set(self,valeur):
        self.valeur = valeur



class Fenêtre1():

    def __init__(self, element):
        self.element = element
        self.text = tk.Label(element,font =('Impact', 25),width= 10, text = "SUDOKU", fg ="black", bg = "#A39F9E")
        self.menu = ttk.Combobox(element,values= ["Facile", "Moyen","Difficile"], width = 20)
        self.menu.set("Sélectionner un niveau")
        self.entrer = tk.Entry(element, width =13)
        self.load = ttk.Progressbar(root, orient = HORIZONTAL,length = 100)
        self.btn = tk.Button(element, text = " Démarrer !", command =self.Niveau_choix)
        self.text.place(y = 85, x = 160)
        self.menu.place(y = 150, x = 170)
        self.btn.place(y = 400 ,x = 190)
        self.load.place(y = 450 ,x = 175)



    def Niveau_choix(self):
        for i in self.menu['values']:
            if self.menu.get() == i:
                self.chargement()
        None   


    def chargement(self):

        pygame.mixer.music.load("loading.mp3") 
        pygame.mixer.music.play()
        self.load['value'] = 30
        root.update_idletasks() 
        time.sleep(2)

        self.load['value'] = 70
        root.update_idletasks() 
        time.sleep(3) 

        self.load['value'] = 80
        root.update_idletasks() 
        time.sleep(1)

        self.load['value'] = 100
        root.update_idletasks() 
        time.sleep(1.5)
        pygame.mixer.music.stop()
        self.element.withdraw()
        if self.menu.get() == "Facile":
            Grille1()
        if self.menu.get() == "Moyen":
            Grille2()
        if self.menu.get() == "Difficile":
            Grille3()


# Interface menu 

root = tk.Tk()
root["bg"] = "#6AA2C5" 
root.geometry(f'{500}x{500}+{350}+{90}')
lancement = Fenêtre1(root)

#--------------------------- événement Sourie/Clavier ------------------------------------------

#enregistrement des coordonnés du clique 

def compteur1(event):
    global lancementj
    global touche
    global enregistre
    enregistre = (event.x,event.y)
    clique = lancement_j.localisation(enregistre)
    if clique:
        lancement_j.cible1(clique[0] , clique[1])
        touche = None


# interactions avec les touches du clavier 

def chiffre1(event):
    global touche
    global lancement_j
    global chargement

    if event.keysym == '1':
        touche = 1
    if event.keysym == '2':
        touche = 2
    if event.keysym == '3':
        touche = 3
    if event.keysym == '4':
        touche = 4
    if event.keysym == '5':
        touche = 5
    if event.keysym == '6':
        touche = 6
    if event.keysym == '7':
        touche = 7
    if event.keysym == '8':
        touche = 8
    if event.keysym == '9':
        touche = 9
    if event.keysym == 'BackSpace':
        lancement_j.efface1()
        touche = 0
    if event.keysym == 'Return':
        x,y = lancement_j.cible
        chargement_grille1(x,y)

    charge1()       


       
def charge1():
    global lancement_j
    global touche
    if lancement_j.cible and touche != None:
        lancement_j.ajoute1(touche)

def chargement_grille1(a,b):

    global lancement_j
    global fautes
    global chargement
    global touche 


    if lancement_j.carre[a][b].entrer != 0:
        if lancement_j.insere1(lancement_j.carre[a][b].entrer):
            pygame.mixer.music.load("ajoute.mp3") 
            pygame.mixer.music.play()
            time.sleep(0.9)
            pygame.mixer.music.stop()
        else:
            fautes += 1
            pygame.mixer.music.load("faute.mp3") 
            pygame.mixer.music.play()
            time.sleep(0.9)
            if fautes == 4:
                menu1()
                chargement = False
                lancement_j.ferme()

        touche = None
        if lancement_j.terminer1():
            pygame.mixer.music.load("victoire.mp3") 
            pygame.mixer.music.play()
            time.sleep(1)
            pygame.mixer.music.stop()
            menu2()
            chargement = False
            lancement_j.ferme()
            
        construction1(lancement_j)
        root.update_idletasks() 


def Grille1():

    global lancement_j
    global chargement 
    global enregistre
    global touche
    global fautes

    root = tk.Tk() 
    root["bg"] = "black"
    root.geometry(f'{540}x{590}+{350}+{15}')
    lancement_j = Jeux(root,Canvas(root , bg = "white",height = 540 , width = 540),9,9,540,540)
  
    while chargement:
        
        root.bind('<Button-1>',compteur1)
        root.bind('<Key>',chiffre1)
        
        construction1(lancement_j)
        root.update_idletasks() 

#------------------------------grille 2--------------------------#

def compteur2(event):
    global lancementj
    global touche
    global enregistre
    enregistre = (event.x,event.y)
    clique = lancement_j.localisation(enregistre)
    if clique:
        lancement_j.cible2(clique[0] , clique[1])
        touche = None




def chiffre2(event):
    global touche
    global lancement_j
    global chargement

    if event.keysym == '1':
        touche = 1
    if event.keysym == '2':
        touche = 2
    if event.keysym == '3':
        touche = 3
    if event.keysym == '4':
        touche = 4
    if event.keysym == '5':
        touche = 5
    if event.keysym == '6':
        touche = 6
    if event.keysym == '7':
        touche = 7
    if event.keysym == '8':
        touche = 8
    if event.keysym == '9':
        touche = 9
    if event.keysym == 'BackSpace':
        lancement_j.efface2()
        touche = 0
    if event.keysym == 'Return':
        x,y = lancement_j.cible
        chargement_grille2(x,y)

    charge2()       




        
def charge2():
    global lancement_j
    global touche
    if lancement_j.cible and touche != None:
        lancement_j.ajoute2(touche)

def chargement_grille2(a,b):

    global lancement_j
    global fautes
    global chargement
    global touche 


    if lancement_j.carre1[a][b].entrer != 0:
        if lancement_j.insere2(lancement_j.carre1[a][b].entrer):
            pygame.mixer.music.load("ajoute.mp3") 
            pygame.mixer.music.play()
            time.sleep(0.9)
            pygame.mixer.music.stop()
        else:
            fautes += 1
            pygame.mixer.music.load("faute.mp3") 
            pygame.mixer.music.play()
            time.sleep(0.9)
            if fautes == 4:
                menu1()
                chargement = False
                lancement_j.ferme()

        touche = None
        if lancement_j.terminer2():
            pygame.mixer.music.load("victoire.mp3") 
            pygame.mixer.music.play()
            time.sleep(1)
            pygame.mixer.music.stop()
            menu2()
            chargement = False
            lancement_j.ferme()
            
        construction2(lancement_j)
        root.update_idletasks() 


def Grille2():

    global lancement_j
    global chargement 
    global enregistre
    global touche
    global fautes

    root = tk.Tk() 
    root["bg"] = "black"
    root.geometry(f'{540}x{590}+{350}+{15}')
    lancement_j = Jeux(root,Canvas(root , bg = "white",height = 540 , width = 540),9,9,540,540)
  
    while chargement:
        
        root.bind('<Button-1>',compteur2)
        root.bind('<Key>',chiffre2)
        
        construction2(lancement_j)
        root.update_idletasks() 


#-------------------------------------grille 3-------------------------------------#


def compteur3(event):
    global lancementj
    global touche
    global enregistre
    enregistre = (event.x,event.y)
    clique = lancement_j.localisation(enregistre)
    if clique:
        lancement_j.cible3(clique[0] , clique[1])
        touche = None
      

def chiffre3(event):
    global touche
    global lancement_j
    global chargement

    if event.keysym == '1':
        touche = 1
    if event.keysym == '2':
        touche = 2
    if event.keysym == '3':
        touche = 3
    if event.keysym == '4':
        touche = 4
    if event.keysym == '5':
        touche = 5
    if event.keysym == '6':
        touche = 6
    if event.keysym == '7':
        touche = 7
    if event.keysym == '8':
        touche = 8
    if event.keysym == '9':
        touche = 9
    if event.keysym == 'BackSpace':
        lancement_j.efface3()
        touche = 0
    if event.keysym == 'Return':
        x,y = lancement_j.cible
        chargement_grille3(x,y)

    charge3()       




        
def charge3():
    global lancement_j
    global touche
    if lancement_j.cible and touche != None:
        lancement_j.ajoute3(touche)

def chargement_grille3(a,b):

    global lancement_j
    global fautes
    global chargement
    global touche 


    if lancement_j.carre2[a][b].entrer != 0:
        if lancement_j.insere3(lancement_j.carre2[a][b].entrer):
            pygame.mixer.music.load("ajoute.mp3") 
            pygame.mixer.music.play()
            time.sleep(0.9)
            pygame.mixer.music.stop()
        else:
            fautes += 1
            pygame.mixer.music.load("faute.mp3") 
            pygame.mixer.music.play()
            time.sleep(0.9)
            if fautes == 4:
                menu1()
                chargement = False
                lancement_j.ferme()

        touche = None
        if lancement_j.terminer3():
            pygame.mixer.music.load("victoire.mp3") 
            pygame.mixer.music.play()
            time.sleep(1)
            pygame.mixer.music.stop()
            menu2()
            chargement = False
            lancement_j.ferme()
            
        construction3(lancement_j)
        root.update_idletasks() 


def Grille3():

    global lancement_j
    global chargement 
    global enregistre
    global touche
    global fautes

    root = tk.Tk() 
    root["bg"] = "black"
    root.geometry(f'{540}x{590}+{350}+{15}')
    lancement_j = Jeux(root,Canvas(root , bg = "white",height = 540 , width = 540),9,9,540,540)
              
    
    while chargement:
        
        root.bind('<Button-1>',compteur3)
        root.bind('<Key>',chiffre3)
        
        construction3(lancement_j)
        root.update_idletasks() 
        
root.mainloop()
