from math import ceil,sqrt

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

def numb_has_prime(a):
    while a>0:
        if is_prime(a%10):
            return True
        a//=10
    return False

def f(T):
    n=len(T)

    for i in range(n):
        flag=True
        for j in range(n):
            if not numb_has_prime(T[i][j]):
                flag = False
                break
        if not flag:
            return False
            
    return True
