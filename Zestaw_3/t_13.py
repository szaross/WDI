def rewers(t):
    t2 = [0 for _ in range(len(t))]
    k=len(t)-1
    for i in range(len(t)):
        t2[i]=t[k]
        k-=1
    return t2



def f(t):
    max_c = 0
    t2 = rewers(t)
    for i in range(len(t)):
        for j in range(len(t)):
            i_cp=i
            licznik=0
            while i_cp<len(t) and j<len(t) and t[i_cp]==t2[j]:
                i_cp+=1
                j+=1
                licznik+=1
            max_c = max(max_c,licznik)
    return max_c




if __name__=="__main__":
    print(f([2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]))