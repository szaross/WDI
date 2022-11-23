def waga(T,masa,p=0):
    if p==len(T):
        return masa==0
    return waga(T,masa-T[p],p+1) or waga(T,masa,p+1)

def f(T,masa):
    return waga(T,masa)