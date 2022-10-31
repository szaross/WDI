def f(t):

    q=t[1]/t[0]
    max_r=0
    licznik=2

    for i in range(1,len(t)-1):
        if t[i+1]/t[i] == q:
            licznik += 1
        else:
            licznik =2
        
        if licznik>max_r:
            max_r=licznik
        q=t[i+1]/t[i]

    return(max_r)