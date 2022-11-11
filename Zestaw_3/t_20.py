from math import sqrt,ceil

def is_prime(a):
    if a<2:
        return False
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

def unique_factors(a):
    i=2
    factors=[]
    while a>1 and i<=ceil(sqrt(a)):
        while a%i==0:
            if i in factors:
                return False
            factors += [i]
            a//=i
        i+=1
    return True

def f(t):
    n=len(t)
    max_length=0

    for i in range(n):
        for j in range(i,n):
            iloczyn =1
            for k in range(j-i+1):
                iloczyn*=t[i+k]

            if unique_factors(iloczyn):
                max_length=max(max_length,j-i+1)
    return max_length
            
if __name__=="__main__":
    x = int(input())
    print(unique_factors(x))