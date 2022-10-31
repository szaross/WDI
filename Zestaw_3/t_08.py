def f(tab):
    def rozklad(a):
        czynniki = []
        while a!=1:
            for i in range(2,a+1):
                if a%i==0:
                    czynniki += [i]
                    a//=i
        return czynniki


    def przejscie(i):
        if i==len(tab)-1:
            print(True)
            exit()
        elif i > len(tab)-1:
            return False
        
        czynniki = rozklad(tab[i])
        for czynnik in czynniki:
            przejscie(i+czynnik)

    przejscie(0)