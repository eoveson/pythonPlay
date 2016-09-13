import collections
from functools import reduce


def AreAnagrams(word1, word2):
    hashtable = collections.defaultdict(int)
    for char in word1:
        hashtable[char] += 1
    for char in word2:
        hashtable[char] -= 1
        if hashtable[char] < 0:
            return False

    return True

print(AreAnagrams("test", "sett"))

arr = [1,3,3,2,5,5,5,7,7]
set1 = set(arr)
print(set1)
list1 = list(set1)
print(list1)
arr = arr+list1
print(arr)
print(reduce(lambda x,y: x^y, arr))
