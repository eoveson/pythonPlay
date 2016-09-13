import collections

def reduceDups(str):
    set1 = set()
    result=[]
    for char in str:
        if char not in set1:
            result+=char
            set1.add(char)
    return ''.join(result)

#print(reduceDups("tree traversal"))

print(" ".join(reversed("this is a test".split())))

