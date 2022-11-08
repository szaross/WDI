def f(T):
    n=len(T)
    a,b=0,n-1
    c=1
    while a<=b:
        for i in range(a,b+1):
            T[a][i]=c
            c+=1
        for i in range(a+1,b):
            T[i][b]=c
            c+=1
        for i in range(b,a,-1):
            T[b][i]=c
            c+=1
        for i in range(b,a,-1):
            T[i][a]=c
            c+=1
        a+=1
        b-=1
    return T

if __name__=="__main__":
    T=[[0 for _ in range(11)] for _ in range(11)]
    print(*f(T),sep='\n')