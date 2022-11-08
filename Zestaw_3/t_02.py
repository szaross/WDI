def bubble_sort(T):
    n=len(T)
    for i in range(n-1):
        for j in range(n-i-1):
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]

def dl_liczby(a: int):
        licznik=0
        while a!=0:
            a//=10
            licznik+=1
        return licznik

def f(a,b):
    sa_zbudowane = True
    tab_a=[0 for _ in range(dl_liczby(a))]
    tab_b=[0 for _ in range(dl_liczby(b))]

    for i in range(dl_liczby(a)):
        tab_a[i]=a%10
        a//=10

    for i in range(dl_liczby(b)):
        tab_b[i]=b%10
        b//=10

    if len(tab_b)!=len(tab_a):
        return False

    bubble_sort(tab_a)
    bubble_sort(tab_b)
    
    for i in range(len(tab_a)):
        if tab_a[i]!=tab_b[i]:
            sa_zbudowane=False

    return sa_zbudowane

if __name__=="__main__":
    print(f(123,123))