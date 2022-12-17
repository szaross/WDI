def czynniki(a):
    czynniki=[]
    for i in range(2,a+1):
        if a%i==0: czynniki.append(i)
        while a%i==0:
            a//=i
    return czynniki

def f(n):
    suma=0
    def iloczyn(T,T1=[],i=0):
        nonlocal suma
        if i==len(T):
            if T1:
                wynik=1
                for el in T1:
                    wynik*=el
                suma+=wynik
            return
        iloczyn(T,T1+[T[i]],i+1)
        iloczyn(T,T1,i+1)

    iloczyn(czynniki(n))
    return suma