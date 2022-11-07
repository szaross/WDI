def f(T,k):
    knight_moves=[(1,2),(-1,2),(2,1),(2,-1)]
    n=len(T)
    counter =0
    for i in range(n):
        for j in range(n):
            for move in knight_moves:
                if 0<=i+move[0]<n and 0<=j+move[1]<n:
                    if T[i][j]*T[i+move[0]][j+move[1]]==k:
                        counter+=1
    return counter
