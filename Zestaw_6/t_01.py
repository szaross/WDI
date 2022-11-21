from math import ceil,sqrt,log10

def is_prime(a):
    if a<2: return False
    if a==2 or a==3: return True
    if a%2==0 or a%3==0: return False
    i=5
    while i<=ceil(sqrt(a)):
        if a%i==0:
            return False
        i+=2
        if a%i==0:
            return False
        i+=4
    return True

def wykresl(a,n=0):
    if dl(a)<n+2:
        return 
    if is_prime(a):
        print(a)
    wykresl(a,n+1)
    wykresl(usun(a,n),0)


def usun(a,n):
    prawo = a%(10**n)
    lewo = a//(10**(n+1))
    liczba = (lewo*(10**n))+prawo
    return liczba
    
def dl(a):
    licznik =0
    while a>0:
        a//=10
        licznik+=1
    return licznik
if __name__=="__main__":
    #print(enta(123456789,3))
    # for i in range(9):
    #     print(usun(123456789,i))
    wykresl(1437)