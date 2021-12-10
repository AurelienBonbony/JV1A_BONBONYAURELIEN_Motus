import random
from colorama import Fore, Back, Style
from colorama import init
init()
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

liste = ["cahier", "ours", "bois", "hydre", "table","outil", "broyeur", "lutin", "peur", "devoir"]
mot = random.choice(liste)
tentative = 8
affichage = ""
lettreTrouvee = ""

for i in mot:
    affichage = affichage + ". "

print("Bienvenue au jeu du Motus !")

while tentative > 0:
    print("\nMot à deviner : ", affichage)
    proposition = input("proposez une lettre : ")
     
    if proposition in mot:
        tentative = tentative - 1
        lettreTrouvee = (Fore.RED + lettreTrouvee) + proposition
        print(mot.index(proposition))
        init(autoreset=True)
        print(Fore.RED + proposition)
        print("Correct ! il vous reste", tentative, "tentatives !")
    else:
        tentative = tentative - 1
        init(autoreset=True)
        print(Fore.BLUE + proposition)
        print("Dommage, la lettre n'est pas dans le mot, il vous reste", tentative, "tentatives !")
           

    affichage = ""
    for x in mot:
        if x in lettreTrouvee:
            affichage = affichage + x + " "
        else:
            affichage = affichage + ". "

    if ". " not in affichage:
        print("Vous avez réussi!")
        break
print(">>", mot, "<<")
print(":Fin de partie:")
