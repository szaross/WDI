def suma(T,sum,w=0):
    n=len(T)
    if sum<0 or not T or not T[0]:
        return False
    if sum==0:
        return True
    for i in range(n):
        if suma(trans(T,w,i),sum-T[w][i]):
            return True
    return False


def trans(T,w,k):
    new = [[0 for _ in range(len(T)-1)] for _ in range(len(T)-1)]
    i=0
    m=0
    while m<len(T) and i<len(T)-1:
        j=0
        n=0
        flag = False
        while n<len(T) and j<len(T)-1:
            if m!=w and n!=k:
                new[i][j]=T[m][n]
                flag=True
                j+=1
            n+=1
        if flag:
            i+=1
        m+=1
        
    return new

if __name__=="__main__":
    print(trans([[1,2,3],[4,5,6],[7,8,9]],1,1))


def f(T,a):
    return suma(T,a)