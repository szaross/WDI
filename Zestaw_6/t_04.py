from time import sleep
def canMove(T,w,k):
    moves=[(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1)]
    available=[]
    n=len(T)
    for move in moves:
        if 0<=move[0]+w<n and 0<=move[1]+k<n and T[move[0]+w][move[1]+k]==0:
            available.append(move)
    return available

def skoczek(T,w,k,i=1):
    T[w][k]=i
    if i==len(T)**2:
        print(*T,sep="\n")
        exit()

    moves=canMove(T, w, k)
    for move in moves:
        skoczek(T, w+move[0], k+move[1],i+1)
    T[w][k]=0

def f(n):
    T=[[0 for _ in range(n)] for _ in range(n)]
    return skoczek(T, 0, 0)

if __name__=="__main__":
    print(f(6))

    