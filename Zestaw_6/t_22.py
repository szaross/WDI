from math import ceil,sqrt

def czynniki(a):
    czynniki = []
    for i in range(2,a):
       # print(i)
        while a%i==0:
            if i not in czynniki:
                czynniki+=[i]
            a//=i
    return czynniki


def skok(T,i=0,sum=0):
    if i==len(T)-1:
        return sum
    if i>=len(T):
        return -1
    czyn=czynniki(T[i])
    for c in czyn:
        p =skok(T,i+c,sum+1)
        if p!=-1:
            return p
    return -1

def f(T):
    return skok(T)

if __name__=="__main__":
    print(czynniki(15))