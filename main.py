# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

pola=['#','#','#','#','#','#','#','#','#','#']
tura=0
gra=True

def wyswietlplansze(pola):
    plansza = """
    ___________________
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  5  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  1  |  2  |  3  |
    |     |     |     |
    |-----------------|
    """
    for i in range(1,10):
        if (pola[i] == 'O' or pola[i]=='X'):
            plansza = plansza.replace(str(i),pola[i])
        else:
            plansza = plansza.replace(str(i), ' ')
    print(plansza)


def zaznacz(tura,pola):
    if tura==0:
        ruch=int(input("Ruch Gracz,wybierz pole:"))
        if pola[ruch]!='#':
            print("Pole juz zajete,wybierz jeszcze raz")
            zaznacz(tura,pola)
        else: pola[ruch]='X'

    elif tura==1:
        ruch=random.randint(1,10)
        if pola[ruch]!='#':
            ruch=random.randint(1,10)
        else: pola[ruch]='O'

    return pola

def wygrana(plansza,mark):
    if plansza[1] == plansza[2] == plansza[3] == mark:
        return True
    if plansza[4] == plansza[5] == plansza[6] == mark:
        return True
    if plansza[7] == plansza[8] == plansza[9] == mark:
        return True
    if plansza[1] == plansza[4] == plansza[7] == mark:
        return True
    if plansza[2] == plansza[5] == plansza[8] == mark:
        return True
    if plansza[3] == plansza[6] == plansza[9] == mark:
        return True
    if plansza[1] == plansza[5] == plansza[9] == mark:
        return True
    if plansza[3] == plansza[5] == plansza[7] == mark:
        return True
    return False


while gra==True:
    zaznacz(tura,pola)
    wyswietlplansze(pola)

    if tura==0:
        if wygrana(pola,'X')==True:
            print('Wygral Gracz,gratulacje')
            gra=False
        tura=1
    else:
        if wygrana(pola,'O')==True:
            print('Wygral Komputer,sprobuj nastepnym razem')
            gra=False
        tura=0






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
