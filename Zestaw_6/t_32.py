def f(T,k):
    flag=False

    def subset(T,k,T1=[],T2=[],i=0):
        nonlocal flag
        if len(T1)==len(T2)==k and sum(T1)==sum(T2):
            flag=True
            return True
        if i==len(T):
            return False
        if not flag:
            return subset(T,k,T1+[T[i]],T2,i+1) or subset(T,k,T1,T2+[T[i]],i+1) or subset(T,k,T1,T2,i+1)
    
    return subset(T, k)

