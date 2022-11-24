def rozklad(liczba,suma=0,p=1,final=""):
    if suma==liczba:
        print(final[:-1])
    if suma>liczba or p>=liczba:
        return
    
    rozklad(liczba,suma+p,p,final+f'{p}+')
    rozklad(liczba,suma,p+1,final)

def f(a):
    rozklad(a)

if __name__=="__main__":
    rozklad(10)