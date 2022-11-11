def f():
    a,b=0,1
    while a<1000000:
        print(a)
        a,b=b,a+b
    return

if __name__=="__main__":
    f()