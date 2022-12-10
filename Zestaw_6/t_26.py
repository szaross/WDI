from math import sqrt,ceil

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

def bin_to_dec(a):
    dec=0
    i=0
    while a>0:
        l=a%10
        dec=dec + l*(2**i)
        a//=10
        i+=1
    return dec

def f(A,B):
    count=0
    def build(A,B,num=1):
        nonlocal count
        if A==0 and B==0:
            print(num)
            if not is_prime(bin_to_dec(num)):
                count+=1
        if A>0:
            build(A-1,B,(num*10)+1)
        if B>0:
            build(A,B-1,num*10)

    build(A-1,B)
    return count

if __name__=="__main__":
    print(f(5,5)) #109