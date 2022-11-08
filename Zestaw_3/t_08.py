def rozklad(a):
        czynniki = []
        while a>1:
            for i in range(2,a+1):
                if a%i==0:
                    czynniki += [i]
                    a//=i
        return czynniki

def f(T):
    n=len(T)
    tmp=[False for _ in range(n)]
    tmp[0]=True
    for i in range(n):
        if tmp[i]:
            czynniki=rozklad(T[i])
            for c in czynniki:
                if i+c<n:
                    tmp[i+c]=True
    return tmp[n-1]

if __name__=="__main__":
    print(f([2,2,3,4,5,7]))