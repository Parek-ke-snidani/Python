import random

hodnoty = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
barvy = ["♠","♥","♦","♣"]

balicek = [h +b for h in hodnoty for b in barvy]
random.shuffle(balicek)

hrac=[]
dealer=[]
def rozdani_karet(hrac, dealer, balicek):
    hrac.append(balicek.pop())
    dealer.append(balicek.pop())
    hrac.append(balicek.pop())
    dealer.append(balicek.pop())
    return hrac, dealer, balicek

hrac, dealer, balicek = rozdani_karet(hrac, dealer, balicek)

print(f"Hráč: {hrac[0]}, {hrac[1]}")
print(f"Dealer: {dealer[0]}")

def dalsi_karta(hrac, balicek):
    hrac.append(balicek.pop())
    return hrac, balicek

def hodnota(karty):
    hodnota = 0
    esa = 0

    for karta in karty:
        cislo = karta[:-1]

        if cislo =="A":
            esa += 1
        elif cislo in ("J", "Q", "K"):
            hodnota += 10
        else:
            hodnota += int(cislo)

    for A in range(esa):
        if hodnota + 11 <= 21:
            hodnota += 11
        else:
            hodnota += 1

    return hodnota

def tah_hrace(hrac, balicek):
    while True:
        volba = input("Chceš další kartu? (ano/ne): ").lower().strip()
        if volba in ("ano", "yes", "y", "a", "dalsi", "karta", "kartu"):
            hrac, balicek = dalsi_karta(hrac, balicek)
            print("Hráč:", ", ".join(hrac))
        elif volba in ("ne", "n", "stop", "zastav", "stojim"):
            print("Hráč zůstává, hraje dealer.")
            break
        else:
            print("Neplatná volba, napiš 'ano' nebo 'ne'.")
    return hrac, balicek

def tah_dealera(dealer, hrac, balicek):
    while True:
        hodnota_dealer = hodnota(dealer)
        hodnota_hrac = hodnota(hrac)
        if hodnota_hrac > 21:
            break
        elif hodnota_dealer < hodnota_hrac:
            dealer.append(balicek.pop())
        else:
            print("Dealer ukončil svůj tah")
            print("Dealer", ", ".join(dealer))
            break
    return dealer, hrac, balicek
            
hrac, balicek = tah_hrace(hrac, balicek)

dealer, hrac, balicek = tah_dealera(dealer, hrac, balicek)

def check_win(hrac, dealer):
    hodnota_dealer = hodnota(dealer)
    hodnota_hrac = hodnota(hrac)
    if hodnota_dealer > 21:
        print(f"Hráč: {hodnota_hrac}")
        print(f"Dealer: {hodnota_dealer}")
        print("Hráč vyhrál")
    elif hodnota_hrac > 21:
        print(f"Hráč: {hodnota_hrac}")
        print(f"Dealer: {hodnota_dealer}")
        print("Dealer vyhrál")
    elif hodnota_hrac > hodnota_dealer:
        print(f"Hráč: {hodnota_hrac}")
        print(f"Dealer: {hodnota_dealer}")
        print("Hráč vyhrál")
    elif hodnota_hrac == hodnota_dealer:
        print(f"Hráč: {hodnota_hrac}")
        print(f"Dealer: {hodnota_dealer}")
        print("Remíza")
    else:
        print(f"Hráč: {hodnota_hrac}")
        print(f"Dealer: {hodnota_dealer}")
        print("Dealer vyhrál")

check_win(hrac, dealer)

print("Dealer:", ", ".join(dealer))
print("hráč:", ", ".join(hrac))




