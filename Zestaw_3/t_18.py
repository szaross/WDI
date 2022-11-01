def f(t):
    length=0
    n=len(t)
    for i in range(n):
        for j in range(i+1,n):
            flag=True
            for k in range(j-i+1):
                if t[k+i]%2==0 or t[k+i]!=t[j-k]:
                    flag=False
                    break
            if j-i+1>length and flag:
                length=j-i+1
    return length