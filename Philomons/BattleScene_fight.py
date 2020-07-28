#module import / Importation des modules-----------------------------------------------

import pygame
import BattleScene_Classes as bc
import os
import random


#initial variables/ variables initiales---------------------------------------------------

current_dir = os.getcwd()
continuer = True

resolution = (650,550)
pygame.init()

txt =  bc.UI_text()

font = pygame.font.Font(current_dir + "/Ressources/Fonts/slkscr.ttf", 30)
font2 = pygame.font.Font(current_dir + "/Ressources/Fonts/slkscr.ttf", 19)
philoselfnum = random.randint(1,len(bc.PhList)-1)


#Philomons in fight/ Philomons en combat----------------------------------------------------

#MONPHILOMON = bc.PokemonInFight(philoselfnum)
MONPHILOMON = bc.PokemonInFight(10)
#AUTRE = bc.PokemonInFight(random.randint(1,len(bc.PhList)-1))
AUTRE = bc.PokemonInFight(9)

#Choice Text/Textes_choix-----------------------------------------------------------

texte1 = font.render(txt.text1 , True, (0, 0, 0))
texte2 = font.render(txt.text2 , True, (0, 0, 0))
texte3 = font.render(txt.text3 , True, (0, 0, 0))
texte4 = font.render(txt.text4 , True, (0, 0, 0))



#attack dialogue/dialogue_attaque-------------------------------------------------------

texteAttack = ["Your Philomon attacks !","Il utilise !","the enemy philomon attacks !","Il utilise !" ,"Your turn !"]

texte5 = font.render("Your Philomon attacks !" , True, (0, 0, 0))

#escape dialogue/dialogue fuite

texte6 = font.render("You can't escape !", True, (0,0,0))

#philomon  dialogue/ Dialogue philomons

texte7 = font.render("You only have one Philomon !", True, (0,0,0))

#bag dialogue/Dialogue sac

texte8 = font.render("You don't have a bag !", True, (0,0,0))

#Victory defeat dialogue/Dialogue Victoire-defaite

textedef = ["Your Philomon is KO !", "You lost !"]

textevic = ["The enemy Philomon is KO !", "You won !"]

texte9 =  font.render("Fini !", True, (0,0,0))
#Philomons names/Noms philomons---------------------------------------------------------

philomonJ1Name = font2.render(MONPHILOMON.pokemonName , True, (0, 0, 0))
philomonJ2Name = font2.render(AUTRE.pokemonName , True, (0, 0, 0))

ecran = pygame.display.set_mode(resolution)

#loading images/chargement des images------------------------------------------------------------------
back = bc.Backgrounds()
background_img = pygame.image.load(back.back ).convert_alpha()
background_img = pygame.transform.scale(background_img, (650, 450))

pokepath = current_dir + "\\Ressources\\Philomons\\" + AUTRE.pokemonSprite
pokeImage = pygame.image.load(pokepath).convert_alpha()
pokeImage = pygame.transform.scale(pokeImage, (250,250))

pokepath2 = current_dir + "\\Ressources\\Philomons\\" + MONPHILOMON.pokemonSprite
pokeImage2 = pygame.image.load(pokepath2).convert_alpha()
pokeImage2 = pygame.transform.scale(pokeImage2, (250,250))

UIbox = current_dir + "\\Ressources\\UI\\ui_boxes.png"
Uimage = pygame.image.load(UIbox).convert_alpha()
Uimage = pygame.transform.scale(Uimage, (650,450))

UIbox2 = current_dir + "\\Ressources\\UI\\dialogbox.png"
Uimage2 = pygame.image.load(UIbox2).convert_alpha()
Uimage2 = pygame.transform.scale(Uimage2, ( 704, 250))


cursor = bc.UI_cursor()
cursorimage = pygame.image.load(cursor.cursori).convert_alpha()
cursorimage = pygame.transform.scale(cursorimage, ( 40, 40))

#sounds/Sons---------------------------------------------------------------------------

clingselection = pygame.mixer.Sound(current_dir + "\\Ressources\\sons\\Selection_Click_Beep.wav")
damagesound = pygame.mixer.Sound(current_dir + "\\Ressources\\sons\\Hit_Damage.wav")
boostsound = pygame.mixer.Sound(current_dir + "\\Ressources\\sons\\Boost_sound.wav")


#Functions/Fonctions----------------------------------------------------------------------

def Attaquer(vie, att, defense, nameattack, defenseself):

    specificite_att = bc.AttDict[nameattack]

    if (specificite_att[0] == 0):
        boostsound.play()
    else :
        damagesound.play()
    vie -= ((2.4 * att/ defense*50) + 2) * (specificite_att[0]/100)

    att += specificite_att[1]
    att -= specificite_att[3]
    if att < 10 :
        att = 10
    defenseself += specificite_att[2]
    defenseself -= specificite_att[4]
    if defenseself < 10 :
        defenseself = 10

    return vie, att, defenseself

#variable at start ------------------------------------------------------------

pvJ1_start = MONPHILOMON.pv
pvJ2_start = AUTRE.pv
largebar_start = 122

step = 0
selection = True
attacking = False
escaping = False
bag = False
mons = False
cursor.zone = 1
endofthefight = False
finishing = False
didOnce = False
J1_faster = 0
attackname = "basename"
attacknameother = "basename"


if (MONPHILOMON.speed > AUTRE.speed) :
    J1_faster = 1
elif(MONPHILOMON.speed < AUTRE.speed) :
    J1_faster = 0
else:
    J1_faster = random.randint(0,1)

#Main program/Programme principal------------------------------------------------------------

while continuer == True :
    #Inputs/Touches appuyées
    for event in pygame.event.get() :
        #Quit the game/quitte le jeu--------------------
        if event.type == pygame.QUIT :
            continuer = False
        #Move the cursor/Bouge le curseur -------------
        if event.type == pygame.KEYDOWN :
            clingselection.play()
            if event.key ==pygame.K_LEFT:

                cursor.left()

            if event.key ==pygame.K_RIGHT:
                cursor.right()

            if event.key ==pygame.K_UP:
                cursor.up()

            if event.key ==pygame.K_DOWN:
                cursor.down()

            #Choose something/Choisit qqch -------------
            if event.key == pygame.K_RETURN:
                didOnce = False
                #a means attack zone, p means philomon zone, f means escape zone, s means bag zone/ a = zone attaque, p = zone philomon, f = zone fuite, s= zone sac
                if selection == True :
                    if cursor.zone == 1 :
                        if cursor.selected == "a" :
                            txt.Menu_Attack(MONPHILOMON.attack1, MONPHILOMON.attack2, MONPHILOMON.attack3, MONPHILOMON.attack4)
                            texte1 = font.render(txt.text1 , True, (0, 0, 0))
                            texte2 = font.render(txt.text2 , True, (0, 0, 0))
                            texte3 = font.render(txt.text3 , True, (0, 0, 0))
                            texte4 = font.render(txt.text4 , True, (0, 0, 0))
                            cursor.zone = 2
                        if cursor.selected == "p":
                            selection = False
                            mons = True
                            step = 0

                        if cursor.selected == "f" :
                            selection = False
                            escaping = True
                            step = 0
                        if cursor.selected == "s" :
                            selection = False
                            escaping = False
                            bag = True
                            step = 0

                    elif cursor.zone == 2 :

                        if cursor.selected == "a" :
                            selection = False
                            attackname = MONPHILOMON.attack1

                            attacking = True
                            step = 0
                        if cursor.selected == "p" :
                            selection = False
                            attackname = MONPHILOMON.attack2

                            attacking = True
                            step = 0
                        if cursor.selected == "f" :
                            selection = False
                            attackname = MONPHILOMON.attack4

                            attacking = True
                            step = 0
                        if cursor.selected == "s" :
                            selection = False
                            attackname = MONPHILOMON.attack3

                            attacking = True
                            step = 0
                else :
                    step += 1

            if (event.key == pygame.K_ESCAPE) :
                cursor.zone = 1
                txt.Menu_Principal()
                texte1 = font.render(txt.text1 , True, (0, 0, 0))
                texte2 = font.render(txt.text2 , True, (0, 0, 0))
                texte3 = font.render(txt.text3 , True, (0, 0, 0))
                texte4 = font.render(txt.text4 , True, (0, 0, 0))

    #display screen/ affiche l'écran ----------------------------------------------------------

    ecran.blit(background_img,(0, 0))

    #layer2/couche2-------------------------

    ecran.blit(pokeImage, (375,50))
    ecran.blit(pokeImage2, (10,175))


    #layer3 health bars /couche3 Barre de vie-----------------------

    ecran.blit(Uimage, (0,50))
    ecran.blit(Uimage2, (-32,350))

    #Draw the bar of the other philomon/ Dessine la barre de l'autre philomon---
    pygame.draw.rect(ecran, (255, 255, 255), (130, 140, 122, 8))
    if (AUTRE.pv > 0) :
        percentoflifeJ2 = (AUTRE.pv * 122) / pvJ2_start
        if (AUTRE.pv > pvJ2_start / 2):
            pygame.draw.rect(ecran, (0, 255, 0), (130, 140, percentoflifeJ2, 8))
        elif (AUTRE.pv <= pvJ2_start / 4):
            pygame.draw.rect(ecran, (255, 0, 0), (130, 140, percentoflifeJ2, 8))
        elif (AUTRE.pv <= pvJ2_start / 2):
            pygame.draw.rect(ecran, (255, 165, 0), (130, 140, percentoflifeJ2, 8))

    #Draw the bar of your philomon/ Dessine la barre de votre philomon----------
    pygame.draw.rect(ecran, (255, 255, 255), (513, 321, 122, 8))

    if (MONPHILOMON.pv > 0) :
        percentoflifeJ1 = (MONPHILOMON.pv * 122) / pvJ1_start

        if (MONPHILOMON.pv > pvJ1_start / 2):
            pygame.draw.rect(ecran, (0, 255, 0), (513, 321, percentoflifeJ1, 8))
        elif (MONPHILOMON.pv <= pvJ1_start / 4):
            pygame.draw.rect(ecran, (255, 0, 0), (513, 321, percentoflifeJ1, 8))
        elif (MONPHILOMON.pv <= pvJ1_start / 2):
            pygame.draw.rect(ecran, (255, 165, 0), (513, 321, percentoflifeJ1, 8))


    #Write the name of the philomons /Ecrit les noms des philomons--------------

    ecran.blit(philomonJ2Name, (50,110))
    ecran.blit(philomonJ1Name, (420,299))

    #layer4/couche4 ------------------------

    #Selection menu /Menu Selection-----------------

    if (selection == True and endofthefight == False) :
        ecran.blit(texte1, (50,426))
        ecran.blit(texte2, (350,426))
        ecran.blit(texte3, (50,501))
        ecran.blit(texte4, (350,501))
        ecran.blit(cursorimage, (cursor.posX,cursor.posY))

    #Attack /Attaque-----------------------
    elif (attacking == True and endofthefight == False) :
        if (J1_faster ==1):
            texteAttack[0] = "Your Philomon attacks !"
            texteAttack[2] = "the enemy Philomon attacks !"
        else :
            texteAttack[0] = "the enemy Philomon attacks !"
            texteAttack[2] = "Your Philomon attacks !"

        if (step == 0):
            texte5 = font.render(texteAttack[step], True, (0, 0, 0))
            ecran.blit (texte5, (50, 475))

        elif (step == 1):
            if (didOnce == False):
                #algo pour calculer longueur barre de vie
                resultlifemoins = largebar_start - int((largebar_start * AUTRE.pv )/ (pvJ1_start))/2
                if (J1_faster==1):
                    texteAttack[1] = "He uses " + str(attackname) + " !"
                    AUTRE.pv, MONPHILOMON.att, MONPHILOMON.defense = Attaquer(AUTRE.pv, MONPHILOMON.att, AUTRE.defense, attackname, MONPHILOMON.defense)
                else :
                    advchoix = [AUTRE.attack1, AUTRE.attack2, AUTRE.attack3, AUTRE.attack4]
                    advfinalchoice = random.randint(0, 3)
                    texteAttack[1] = "He uses " + str(advchoix[advfinalchoice]) + " !"
                    MONPHILOMON.pv, AUTRE.att, AUTRE.defense = Attaquer(MONPHILOMON.pv, AUTRE.att, MONPHILOMON.defense,advchoix[advfinalchoice], AUTRE.defense)

                didOnce = True

            texte5 = font.render(texteAttack[step], True, (0, 0, 0))
            ecran.blit(texte5, (50, 475))

        elif (step == 2):

            texte5 = font.render(texteAttack[step], True, (0, 0, 0))
            ecran.blit(texte5, (50, 475))

        elif (step == 3):
            if (didOnce == False):
                if (J1_faster==1):
                    advchoix = [AUTRE.attack1, AUTRE.attack2, AUTRE.attack3, AUTRE.attack4]
                    advfinalchoice = random.randint(0,3)
                    texteAttack[3] = "He uses " + str(advchoix[advfinalchoice]) + " !"
                    MONPHILOMON.pv, AUTRE.att, AUTRE.defense = Attaquer(MONPHILOMON.pv, AUTRE.att, MONPHILOMON.defense, advchoix[advfinalchoice], AUTRE.defense)
                else :
                    texteAttack[3] = "He uses " + str(attackname) + " !"
                    AUTRE.pv, MONPHILOMON.att, MONPHILOMON.defense = Attaquer(AUTRE.pv, MONPHILOMON.att, AUTRE.defense,attackname, MONPHILOMON.defense)

                didOnce = True

            texte5 = font.render(texteAttack[step], True, (0, 0, 0))
            ecran.blit(texte5, (50, 475))

        elif (step == 4):

            texte5 = font.render(texteAttack[step], True, (0, 0, 0))
            ecran.blit(texte5, (50, 475))

        if step >= 5 :
            cursor.zone = 1
            txt.Menu_Principal()
            selection = True
            escaping = False
            attacking = False
            texte1 = font.render(txt.text1 , True, (0, 0, 0))
            texte2 = font.render(txt.text2 , True, (0, 0, 0))
            texte3 = font.render(txt.text3 , True, (0, 0, 0))
            texte4 = font.render(txt.text4 , True, (0, 0, 0))

    #Escape/Fuite------------------------------------------------------------
    elif (escaping == True and endofthefight == False) :
        if (step == 0) :
            ecran.blit(texte6, (50,475))

        if (step >= 1) :
            cursor.zone = 1
            txt.Menu_Principal()
            selection =True
            escaping = False
            attacking = False
    #Philomons---------------------------------------------------------------
    elif (mons == True and endofthefight == False):
        if (step == 0) :
            ecran.blit(texte7, (50,475))

        if (step >= 1) :
            cursor.zone = 1
            txt.Menu_Principal()
            selection =True
            escaping = False
            attacking = False
            mons = False
    #Bag/Sac------------------------------------------------------------------
    elif (bag == True and endofthefight == False):
        if (step == 0) :
            ecran.blit(texte8, (50,475))

        if (step >= 1) :
            cursor.zone = 1
            txt.Menu_Principal()
            selection =True
            escaping = False
            attacking = False
            bag = False


    #Defeat/Defaite------------------------------------------------------
    if MONPHILOMON.pv <= 0 :
        if (endofthefight == False) :
            finishing = True
            step = 0
            endofthefight =True

        if (finishing == True):
            if (step == 0):
                texte9 = font.render(textedef[step], True, (0, 0, 0))
                ecran.blit(texte9, (50,475))

            if (step == 1):
                texte9 = font.render(textedef[step], True, (0, 0, 0))
                ecran.blit(texte9, (50, 475))

            if (step >= 2):
                ecran.blit(texte9, (50, 475))
                continuer = False

    #Victory/Victoire-----------------------------------------------------
    elif AUTRE.pv <= 0 :

        if (endofthefight == False) :
            finishing = True
            step = 0
            endofthefight =True

        if (finishing == True):
            if (step == 0):
                texte9 = font.render(textevic[step], True, (0, 0, 0))
                ecran.blit(texte9, (50,475))
            if (step == 1):
                texte9 = font.render(textevic[step], True, (0, 0, 0))
                ecran.blit(texte9, (50, 475))

            if (step >= 2):
                ecran.blit(texte9, (50, 475))
                continuer = False

    pygame.display.flip()


pygame.quit()
