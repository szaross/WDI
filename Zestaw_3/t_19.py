def f(t):
    max_length=0
    n=len(t)
    for i in range(n):
        for j in range(i,n):
            flag = True
            sum_of_el=0
            sum_of_ind=((i+j)/2)*(j-i+1)

            for k in range(j-i):
                if t[i+k]>=t[i+k+1]:
                    flag=False
                    break
                sum_of_el+=t[i+k]

            sum_of_el+=t[j] #bo nie zsumuje sie ostatni element
            if flag and sum_of_el==sum_of_ind:
                max_length = max(max_length,j-i+1)

    return max_length
