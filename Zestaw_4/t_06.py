def f(T1):
    n=len(T1)
    T2 = [0 for _ in range(n*n)]

    # finding max of T1
    max_numb=0
    for i in range(n):
        for j in range(n):
            if T1[i][j]>max_numb:
                max_numb=T1[i][j]

    # counting how many times a number has appeared in T1
    tmp = [0 for _ in range(max_numb+1)]
    for i in range(n):
        for j in range(n):
            tmp[T1[i][j]]+=1

    count=0
    for i in range(len(tmp)):
        if tmp[i]==1:
            T2[count]=i
            count+=1

    return T2

if __name__=="__main__":
    T = [[1,2,3],[2,3,4],[5,5,6]]
    print(f(T))