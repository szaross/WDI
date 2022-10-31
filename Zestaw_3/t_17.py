from math import sqrt, ceil

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



def f(t1,t2):
    c1 = [0 for _ in range(len(t1))]
    c2 = [0 for _ in range(len(t2))]

    for i in range(len(t1)):
        for j in range(1,3):
            if j==1:
                for k in range(1,3):
                    if k==1:
                        c1[i]==1
                    else:
                        c2[i]==1
            else:
                c1[i]==1
                c2[i]==1
        
            

