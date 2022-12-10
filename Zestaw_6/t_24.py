from math import sqrt

def srodek_ciezkosci(T):
    n=len(T)
    suma_x,suma_y=0,0
    for el in T:
        suma_x+=el[0]
        suma_y+=el[1]
    return (suma_x/n,suma_y/n)

def najm_srodek(T,T1=[],T2=[],i=0):
    if i>len(T)-1:
        if T1 and T2:
            x1,y1=srodek_ciezkosci(T1)
            x2,y2=srodek_ciezkosci(T2)
            return sqrt((x2-x1)**2+(y2-y1)**2)
        else:
            return float('inf')
    return min(najm_srodek(T,T1+[T[i]],T2,i+1),najm_srodek(T,T1,T2+[T[i]],i+1),najm_srodek(T,T1,T2,i+1))

def f(T):
    return najm_srodek(T)