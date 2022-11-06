def f(T):
    max_sum=-1
    col,row=0,0
    n=len(T)
    m=len(T[0])
    for i in range(n):
        for j in range(m):
            sum=0
            if(i+1<n):
                sum+=T[i+1][j]
            if(i-1>=0):
                sum+=T[i-1][j]
            if(j+1<m):
                sum+=T[i][j+1]
            if(j-1>=0):
                sum+=T[i][j-1]
            if(i-1>=0 and j-1>=0):
                sum+=T[i-1][j-1]
            if(i+1<n and j+1<m):
                sum+=T[i+1][j+1]
            if(i+1<n and j-1>=0):
                sum+=T[i+1][j-1]
            if(i-1>=0 and j+1<m):
                sum+=T[i-1][j+1]
            if sum>max_sum:
                max_sum=sum
                row=i
                col=j
           # print(sum)
    return col,row

if __name__=="__main__":
    print(f([[6,6,6],[6,6,6],[6,6,6]]))