def f(a,b):
    # a = int(input("Podaj 1. liczbe naturalna: "))
    # b = int(input("Podaj 2. liczbe naturalna: "))

    def dl_liczby(a: int):
        licznik=0
        while a!=0:
            a//=10
            licznik+=1
        return licznik


    sa_zbudowane = True
    tab_a=[0 for _ in range(dl_liczby(a))]

    for i in range(dl_liczby(a)):
        tab_a[i]=a%10
        a//=10

    for i in range(dl_liczby(b)):
        if b%10 not in tab_a:
            sa_zbudowane = False
            break
        b//=10

    return sa_zbudowane

