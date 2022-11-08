def f(T):
    n=len(T)
    m=len(T[0])
    col_sum=[0 for _ in range(m)]
    row_sum=[0 for _ in range(n)]
  
    for i in range(n):
        for j in range(m):
            row_sum[i]+=T[i][j]

    for i in range(m):
        for j in range(n):
            col_sum[i]+=T[j][i]


    max_col=0
    col=0
    min_row=0

    for i in range(n):
        if row_sum[i]<row_sum[min_row]:
            min_row=i

    for i in range(m):
        if col_sum[i]>col_sum[max_col]:
            max_col=i
    
    
    return [min_row,max_col]