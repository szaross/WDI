from math import sqrt,ceil

def is_prime(a):
    if a==2 or a==3:
        return True
    if a%2==0 or a%3==0 or a==0:
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


def f(t):
    fib=[0 for _ in range(len(t))]
    fib[1]=1

    pierwsza = False
    for i in range(2,len(fib)):
        fib[i]=fib[i-1]+fib[i-2]

    for k in range(len(t)):
        if k in fib:
            if is_prime(t[k]):
                return False
        else:
            if not pierwsza and is_prime(t[k]):
                pierwsza = True

    return pierwsza
                



    

        
