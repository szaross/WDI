from math import log,ceil

def f(n,p):
    number = ['0' for _ in range(ceil(log(n,p))+1)]
    i=-1
    while n>0:
        number[i]=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'][n%p]
        n//=p
        i-=1
    return "".join(number)

if __name__=="__main__":
    print(f(16,2))