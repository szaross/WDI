def one_dig_even(a):
    if a==0:
        return True
    if a>0:
        while a>0:
            if (a%10)%2==0:
                return True
            a//=10
        return False
    else:
        while a<-1:
            if (a%10)%2==0:
                return True
            a//=10
        return False

def f(T):
    N=len(T)
    for i in range(N):
        flag = True
        for j in range(len(T[0])):
            if not one_dig_even(T[i][j]):
                flag = False
                break
        if flag:
            return True
    return False
