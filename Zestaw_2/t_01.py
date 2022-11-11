def f(n):
    a,b=1,1
    x,y=1,1
    c=b
    while c<=n:
        while c*b<=n:
            if c*b==n:
                return True
            a,b=b,a+b
        x,y=y,x+y
        c=y
        a,b=y,x+y
    return False