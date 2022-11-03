def all_odd_num(a):
    if a==0:
        return False
    while a>0:
        if (a%10)%2==0:
            return False
        a//=10
    return True

def f(T):
    N=len(T)
    if len(T[0])==0:
        return False
    for i in range(N):
        flag = False
        for j in range(len(T[0])):
            if all_odd_num(T[i][j]):
                flag= True
                break
        if not flag:
            return False
    return True


if __name__=="__main__":
    print(all_odd_num(0))