import random
from InquirerPy import inquirer
from collections import Counter

hrac =[]
dealer = []

seznam = [1 , 2, 3, 4, 5, 5]
def vyhodnotit_kostky(seznam):
    #Součet
    jednicky = seznam.count(1)
    dvojky = seznam.count(2)
    trojky = seznam.count(3)
    ctverky = seznam.count(4)
    petky = seznam.count(5)
    sestky = seznam.count(6)

    pocty = Counter(seznam)
    #Trojce
    if 3 in pocty.values():
        trojce = True
        return trojce
        
    # Čtveřice
    if 4 in pocty.values():
        ctverice = True
        return ctverice
    
    # fullhouse
    if 3 in pocty.values() and 2 in pocty.values():
        fullhouse = True
        return fullhouse
    
    duplicity = sum(1 for pocet in pocty.values() if pocet > 1)
    if duplicity == 0:
        postupka = True
    elif duplicity == 1 and 2 in pocty.values():
        mala_postupka = True
        

def tah_hrace(kostky):
    for hod in range(5):
        kostky.append(random.randint(1, 6))
    print(kostky)
    for i in range(2):
        prehodit_kostky = input("Chcete přehodit nějaké kostky?").lower().strip()

        if prehodit_kostky in ("ano", "a", "yes", "y"):
            choices = [{"name": f"Kostka {i+1}: {hod}", "value": i} for i, hod in enumerate(kostky)]

            vybrane_kostky = inquirer.checkbox(
                message="Jaké kostky přehodit?",
                choices=choices,
            ).execute()

            for kostky_na_prehoz in vybrane_kostky:
                kostky[kostky_na_prehoz] = random.randint(1, 6)

            print("Nové kostky:", kostky)
        else:
            break


tah_hrace(hrac)