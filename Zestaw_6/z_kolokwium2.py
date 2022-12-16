# Na szachownicy NxN ułożono pewną liczbę pionków, których
# położenie opisuje tablica L=[(w1,k1),(w2,k2),...]. Z lewego
# górnego rogu (w=0,k=0) startuje wieża, która chce dojść do prawego
# dolnego rogu szachownicy. Wieża porusza się tylko w prawo i w dół.
# Wieża nie możże zbić pionka. Napisz funkcję rook(L,N), która
# zwróci minimalną liczbę ruchów potrzebnych wieży, aby dotrzeć
# do celu. Jeżeli jest to niemożliwe funkcja ma zwrócić None.

def rook(T,n):
    def rec(T,n,steps=0,w=0,k=0):
        if w>n-1 or k>n-1 or (w,k) in T:
            return float('inf')
        if w==n-1 and k==n-1:
            return steps
        return min(rec(T,n,steps+1,w,k+1),rec(T,n,steps+1,w+1,k))
    
    if (0,0) in T:
        return None

    val=rec(T,n)
    return val if val != float('inf') else None

if __name__=="__main__":
    T=[(1,1),(2,1)]
    print(rook(T,3))