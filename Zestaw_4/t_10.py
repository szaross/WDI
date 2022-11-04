def f(T):
    n = len(T)

    for i in range(n):
        tmp_flag=False
        for j in range(n):
            if T[i][j]==0:
                tmp_flag=True
                break
        if not tmp_flag:
            return False
    
    for i in range(n):
        tmp_flag=False
        for j in range(n):
            if T[j][i]==0:
                tmp_flag=True
                break
        if not tmp_flag:
            return False
    return True
