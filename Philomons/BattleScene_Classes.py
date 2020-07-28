#module import
import os
import random

current_dir = os.getcwd()

#Get infos from .txt files / récupère les infos depuis les fichiers .txt--------------
with open("Philomons.txt", "r") as f:
    data = f.readlines()

PhList = []
for line in data :
    philo = line.split()
    PhList.append(philo)

with open("AttackProp.txt", "r") as f:
    data = f.readlines()

AttDict = {}

for line in data :

    att = line.split()
    try :
        AttDict[att[0]] = [int(att[1]), int(att[2]), int(att[3]), int(att[4]), int(att[5])]
    except :
        AttDict[att[0]] = [att[1], att[2], att[3], att[4] , att[5]]
#Philomon class/Classe des philomons---------------------------------------------------
class PokemonInFight :
    def __init__(self, num = 1) :
        self.pokemonName = PhList[num][0]
        self.att = int(PhList[num][1])
        self.defense = int(PhList[num][2])
        self.attack1 = PhList[num][3]
        self.attack2 = PhList[num][4]
        self.attack3 = PhList[num][5]
        self.attack4 = PhList[num][6]
        self.pv = int(PhList[num][7])
        self.pokemonSprite = PhList[num][8]
        self.speed = int(PhList[num][9])

#Background class/ classe des arrières-plans-------------------------------------------
class Backgrounds :
    def __init__(self) :
        self.back = current_dir + "\\Ressources\\Background\\" + "back" + str(random.randint(1,9)) + ".png"

#Texts / Textes--------------------------------------------------------------------------
class UI_text :
    def __init__(self) :
        self.text1 = "Attack"
        self.text2 = "Philomons"
        self.text3 = "Bag"
        self.text4 = "Escape"

    def Menu_Attack (self, att1, att2, att3, att4) :
        self.text1 = att1
        self.text2 = att2
        self.text3 = att3
        self.text4 = att4

    def Menu_Principal (self) :
        self.text1 = "Attack"
        self.text2 = "Philomons"
        self.text3 = "Bag"
        self.text4 = "Escape"

#Cursor Class / Classe du curseur
class UI_cursor :
    def __init__(self):
        self.cursori = current_dir + "\\Ressources\\UI\\cursor.png"
        self.posY = 425
        self.selected = "a"
        self.posX = 25
        self.zone = 1
    def left(self) :
        if self.posX == 325 :
            self.posX = 25
            if (self.posY == 500) :
                self.selected = "s"
            else :
                self.selected = "a"
    def right(self) :
        if self.posX == 25 :
            self.posX = 325
            if (self.posY == 500) :
                self.selected = "f"
            else :
                self.selected = "p"
    def up(self) :
        if self.posY == 500 :
            self.posY = 425
            if (self.posX == 25) :
                self.selected = "a"
            else :
                self.selected = "p"
    def down(self) :
        if self.posY == 425 :
            self.posY = 500
            if (self.posX == 25) :
                self.selected = "s"
            else :
                self.selected = "f"

