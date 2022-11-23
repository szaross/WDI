def waga(T,masa,p=0,wybrane=""):
    if p==len(T):
        if masa==0:
            print(wybrane)
        return masa==0
    return waga(T,masa-T[p],p+1,wybrane+str(T[p])+"+\n") or waga(T,masa,p+1,wybrane) or waga(T,masa+T[p],p+1,wybrane+str(T[p])+"-\n")

def f(T,masa):
    return waga(T,masa)

if __name__=="__main__":
    print(f([1,3,4,5,8],11))