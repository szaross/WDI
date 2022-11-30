from math import log10,ceil,inf

def num_len(a):
    if a==0:
        return 1
    counter=0
    while a>0:
        a//=10
        counter+=1
    return counter

def f(T,w=0,k=0): 
    flag=False
    def krol(T,pv,w=0,k=0):
        nonlocal flag
        if w>len(T)-1 or k>len(T[0])-1 or w<0 or k<0:
            return False
        if w==len(T)-1 and k==len(T)-1:
            flag=True
            return True
        if pv>=T[w][k]//(10**(num_len(T[w][k])-1)):
            return False
        if not flag:
            return krol(T,T[w][k]%10,w,k+1) or krol(T,T[w][k]%10,w+1,k+1) or krol(T,T[w][k]%10,w+1,k)
    
    return krol(T,-inf,w,k)

    