def f(t):
    roznica=t[0]-t[1]
    max_r=0
    licznik=2

    for i in range(1,len(t)-1):
        if t[i]-t[i+1] == roznica:
            licznik += 1
        else:
            licznik =2
        
        if licznik>max_r:
            max_r=licznik
        roznica=t[i]-t[i+1]

    return max_r
