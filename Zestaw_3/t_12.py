from random import randint



def f(t):
    last_r=0
    max_dar=1
    max_uar=1
    licznik_dar=2
    licznik_uar=2

    for i in range(len(t)-1):
        roznica = t[i+1]-t[i]

        if roznica == last_r:

            if roznica>0:
                licznik_dar+=1
                if licznik_dar>max_dar:
                    max_dar=licznik_dar

            elif roznica <0:
                licznik_uar+=1
                if licznik_uar>max_uar:
                    max_uar=licznik_uar

        else:
            licznik_dar,licznik_uar=1,1
        last_r = roznica
        if licznik_uar>max_uar:
            max_uar=licznik_uar
        if licznik_dar>max_dar:
            max_dar=licznik_dar
            

    return (max_dar-max_uar)

if __name__=="__main__":
    f(100)