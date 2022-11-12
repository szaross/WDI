# a = int(input("Podaj liczbe: "))

def f(a):
    rosnacy = True
    while a != 0:
        b=a%10
        a=a//10
        if b<=a%10:
            rosnacy= False
            break
    return rosnacy