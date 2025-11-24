import random

cislo = random.randint(1,10)
pocet_pokusu = 0

while True:
    try:
        hrac = int(input("Zadejte číslo: "))
    except ValueError:
        print("To není číslo, zkuste znovu!")
        continue

    pocet_pokusu += 1
    
    if hrac == cislo:
        print(f"Uhádli jste číslo! na {pocet_pokusu} pokusů")
        break
    elif hrac > cislo:
        print("Příliš velké číslo")
    else:
        print("Příliš malé číslo")

