from math import ceil,sqrt

def f(n):
    T=[True for _ in range(n)]
    T[0]=False
    T[1]=False
    num=0
    for i in range(2,ceil(sqrt(n))):
        if T[i]:
            for j in range(i+i,n,i):
                T[j]=False
    for i in T:
        if i:
            num+=1
    return num

if __name__=="__main__":
    f(100)