def digits_set(a):
    digits = []
    while a!=0:
        digits.append(a%10)
        a//=10
    return set(digits)

def f(T):
    n=len(T)
    if n<1:
        return 0
    counter = 0

    for i in range(1,n-1): # without 1st and last columns and rows
        for j in range(1,n-1):
            digits=digits_set(T[i][j])
            if digits_set(T[i-1][j-1])== digits and digits_set(T[i-1][j])== digits and digits_set(T[i-1][j+1])== digits and digits_set(T[i][j+1])== digits and digits_set(T[i+1][j+1])== digits and digits_set(T[i+1][j])== digits and digits_set(T[i+1][j-1])== digits and digits_set(T[i][j-1])== digits:
                counter+=1

    # 1st and last row
    for i in [0,n-1]:
        for j in range(1,n-1):
            digits=T[i][j]
            if digits_set(T[i][j-1])==digits and digits_set(T[i+1][j-1])==digits and digits_set(T[i+1][j])==digits and digits_set(T[i+1][j+1])==digits and digits_set(T[i][j+1])==digits:
                counter+=1
    
    # 1st and last column
    for i in [0,n-1]:
        for j in range(1,n-1):
            digits=T[j][i]
            if digits_set(T[j-1][i])==digits and digits_set(T[j-1][i+1])==digits and digits_set(T[j][i+1])==digits and digits_set(T[j+1][i+1])==digits and digits_set(T[j+1][i])==digits:
                counter+=1
    
    # corners
    digits = digits_set(T[0][0])
    if digits_set(T[0][1])==digits and digits_set(T[1][1])==digits and digits_set(T[1][0])==digits:
        counter +=1
    digits = digits_set(T[0][n-1])
    if digits_set(T[0][n-2])==digits and digits_set(T[1][n-2])==digits and digits_set(T[1][n-1])==digits:
        counter +=1
    digits = digits_set(T[n-1][n-1])
    if digits_set(T[n-2][n-1])==digits and digits_set(T[n-2][n-2])==digits and digits_set(T[n-1][n-2])==digits:
        counter +=1
    digits=digits_set(T[n-1][0])
    if digits_set(T[n-2][0])==digits and digits_set(T[n-2][1])==digits and digits_set(T[n-1][1])==digits:
        counter +=1
    
    return counter