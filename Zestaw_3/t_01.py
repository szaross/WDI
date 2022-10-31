from math import log,ceil
a = int(input("Podaj liczbe naturalna: "))


for i in range(2,17):
    n=a
    licznik = -1
    tab = [0 for _ in range(ceil(log(n,i))+1)]
    while n!=0:
        tab[licznik]=n%i
        licznik -=1
        n=n//i

    print(f"Podstawa {i}: ",end='')
    for el in tab:
        print(el,end='')

    print()