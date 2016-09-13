
def IsPal1(word):
    if word == "": return False
    j = len(word)
    for i in range(j):
        if word[i] != word[j-1]: return False
        if i >= j: break
        j-=1
    return True

#print(IsPal1("aaa"))

def IsPal2(word):
    return word == word[::-1]

#print(IsPal2("faaf"))

def PrintPals(word):
    s = set()
    for i in range(len(word)+1):
        for j in range(i+1, len(word)+1):
            if IsPal1(word[i:j]):
                s.add(word[i:j])
    print(s)

PrintPals("nitin")