def f(T,k):
    n=len(T)
    if n<3: return 0

    for i in range(n):
        for j in range(n):
            for k in range(3,n,2):
                if i+k-1>=n or j+k-1>=n:
                    break
                mult=T[i][j]*T[i+k-1][j+k-1]*T[i][j+k-1]*T[j+k-1][j]
                if mult==k:
                    return True,(i+k-1)/2,(j+k-1)/2
    return False