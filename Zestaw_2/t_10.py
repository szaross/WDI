def f(x):
    a = 2
    istnieje = False

    while a<=x:
        if x%a == 0:
            istnieje = True
            break
        
        a = (3*a) + 1
    return istnieje