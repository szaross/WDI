def check_vowels(w1,w2):
    count1=0
    count2=0
    for w in w1:
        if w in "aeiouy":
            count1+=1
    for w in w2:
        if w in "aeiouy":
            count2+=1
    return count1==count2

def sum_codes(word):
    sum=0
    for c in word:
        sum+=ord(c)
    return sum

def slowo(word,asci_sum,ascii=97,sum=0,final=""):
    if sum==asci_sum and check_vowels(word,final):
            print(final)
            return True
    if ascii>122 or sum>asci_sum:
        return False
    
    return slowo(word,asci_sum,ascii+1,sum+ascii,final+chr(ascii)) or slowo(word,asci_sum,ascii+1,sum,final)


def f(a):
    return slowo(a,sum_codes(a))

if __name__=="__main__":
    print(f('ula'))