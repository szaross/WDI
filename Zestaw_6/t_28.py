def count_ones(T):
    count=0
    for numb in T:
        while numb>0:
            if numb%2==1:
                count+=1
            numb//=2
    return count

def f(T):
    flag=False
    def subset(T,T1=[],T2=[],T3=[],i=0):
        nonlocal flag
        if i==len(T):
            if count_ones(T1)==count_ones(T2)==count_ones(T3):
                flag=True
                return True
            return False
        if not flag:
            return subset(T,T1+[T[i]],T2,T3,i+1) or subset(T,T1,T2+[T[i]],T3,i+1) or subset(T,T1,T2,T3+[T[i]],i+1)
    return subset(T)

if __name__=="__main__":
    print(f([2,3,5,7,15]))