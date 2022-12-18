def f(T):
    sum=0
    max_sum=0
    n_wierszy=len(T)
    n_kolumn=len(T[0])
    for k in range(n_wierszy):
        i=0
        sum=0
        while i<n_kolumn and i<10:
            sum+=T[k][i]
            i+=1
        max_sum=max(sum,max_sum)
        for j in range(0,n_kolumn-10):
            sum=sum-T[k][j]+T[k][j+10]
            max_sum=max(sum,max_sum)
    
    for k in range(n_kolumn):
        i=0
        sum=0
        while i<n_wierszy and i<10:
            sum+=T[i][k]
            i+=1
        max_sum=max(sum,max_sum)
        for j in range(0,n_wierszy-10):
            sum=sum-T[j][k]+T[j+10][k]
            max_sum=max(sum,max_sum)
    return max_sum

if __name__=="__main__":
    print(f([[2], [7], [3], [1], [1]]))