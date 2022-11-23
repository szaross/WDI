def sub(T,p=0,sum=0,ind_sum=0):
    #print(p)
    if p==len(T):
        if sum==0 or sum!=ind_sum:  return float('inf')
        else:   
            #print(sum)
            return sum
    return min(sub(T,p+1,sum+T[p],ind_sum+p),sub(T,p+1,sum,ind_sum))

def f(T):
    x=sub(T)
    if x==float('inf'):   return None
    return x

if __name__=="__main__":
    print(f([1,7,3,5,11,2]))