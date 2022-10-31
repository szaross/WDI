from random import randint

def f(n):

    tab = [randint(1,1000) for _ in range(n)]
    istnieje = False

    def czy_cyfry_niep(a):
        while a>0:
            if a%2==0:
                return False
            a//=10
        return True


    for i in tab:
        if czy_cyfry_niep(i):
            istnieje = True
            break

    #print(istnieje)
    return tab,istnieje

