def f(T,il):
    counter=0

    def iloczyn(T,il,p=0):
        nonlocal counter
        if il==1.0:
            counter+=1
            return
        if p==len(T):
            return

        iloczyn(T,il/T[p],p+1)
        iloczyn(T,il,p+1)
    
    iloczyn(T,il)
    return counter