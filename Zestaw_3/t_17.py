from math import sqrt, ceil,log

def is_prime(a):
    if a==2 or a==3: return True
    if a%2==0 or a%3==0: return False

    i=5
    while i<= ceil(sqrt(a)):
        if a%i==0:
            return False
        i+=2
        if a%i==0:
            return False
        i+=4

    return True

def trojkowy(a,n):
    liczba = [0 for _ in range(n)]
    licznik =-1
    while a!=0:
        liczba[licznik]=a%3
        a//=3
        licznik-=1
    return liczba


def f(t1,t2):
    n=len(t1)
    licznik=0
    for k in range(3**n):
        index=0
        suma=0
        while index<n:
            maska=k%3
            k//=3
            if maska==0:
                suma+=t1[index]+t2[index]
            elif maska==1:
                suma+=t1[index]
            elif maska==2:
                suma=+t2[index]
            index +=1
        if is_prime(suma):
            licznik+=1
    return licznik