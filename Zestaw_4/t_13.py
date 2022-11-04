from math import ceil,sqrt

def is_prime(a):
    if a==2 or a==3:
        return True
    if a%2==0 or a%3==0:
        return False
    i=5
    while i<=ceil(sqrt(a)):
        if a%i==0:
            return False
        i+=2
        if a%i==0:
            return False
        i+=4
    return True

def f(T):
    n=len(T)

    for i in range(n):
        for j in range(n):
            for m in range(n):
                    for p in range(n):
                        if p!=j and m!=i and T[i][j]!=0 and T[m][p]!=0:
                            if is_prime(T[i][j]+T[m][p]):
                                break
                        T[i][j]==0
    return T