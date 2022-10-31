def f(t):
    if len(t)>2:
        min=t[0]
        max=t[1]
    elif len(t)==1:
        return True
    else:
        return False

    min_l=1
    max_l=1

    for i in range(2,len(t)):
        if t[i]>max:
            max=t[i]
            max_l=1
        elif t[i]<min:
            min=t[i]
            min_l=1
        elif t[i]==max:
            max_l+=1
        elif t[i]==min:
            min_l+=1
    
    if min_l==1 and max_l==1:
        return True

    else:
        return False