def f(t):
    max_r=0
    licznik=1

    for i in range(len(t)-1):
        if t[i] < t[i+1]:
            licznik+=1
        else:
            licznik = 1
            
        if licznik>max_r:
            max_r=licznik

    return max_r