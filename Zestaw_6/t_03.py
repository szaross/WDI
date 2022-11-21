def f(T,k):
    return krol(T,k)

def krol(T,k,s=0,w=0):
    n=len(T)
    m=len(T[0])
    if k<0 or k>m-1:
        return float('inf')
    if w==n-1:
        return s + T[w][k]
    return min(krol(T,k-1,s,w+1)+T[w][k],krol(T,k,s,w+1)+T[w][k],krol(T,k+1,s,w+1)+T[w][k])
