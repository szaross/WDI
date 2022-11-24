from math import ceil,sqrt
def is_prime(a):
    if a<2: return False
    if a==2 or a==3: return True
    if a%3==0 or a%2==0:return False
    i=5
    while i<=ceil(sqrt(a)):
        if a%i==0:
            return False
        i+=2
        if a%i==0:
            return False
        i+=4
    return True


def f(a,b):
    counter=0
    
    def zlozenie(a,b,liczba=0,p=1):
        nonlocal counter
        if a==0 and b==0 and is_prime(liczba):
            counter+=1
        if a!=0:
            zlozenie(a//10,b,liczba+((a%10)*p),p*10)
        if b!=0:
            zlozenie(a,b//10,liczba+((b%10)*p),p*10)

    zlozenie(a,b)
    return counter

if __name__=="__main__":
    print(f(123,75))