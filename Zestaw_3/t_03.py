n = int(input("Podaj liczbe naturalna: "))

tab = [i for i in range(0,n+1)]

for x in tab[2:]:
    for z in range(2*x,n+1,x):
        tab[z]=0

for i in tab[2:]:
    if tab[i]!=0:
        print(tab[i],end=' ')