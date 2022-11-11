def nwd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def f(T):
    n=len(T)
    counter=0
    for i in range(n):
        for j in range(i+1,i+3):
            for k in range(j+1,j+3):
                if j<n and k<n:
                    if nwd(nwd(T[i],T[j]),T[k]) == 1:
                        counter +=1
    return counter


