import collections

# find num not present in 2nd array
def numNotPresent(ary1, ary2):
    hash = collections.defaultdict(int)
    for i in ary2:
        hash[i]+=1
    for i in ary1:
        if hash[i] is None or hash[i]==0:
            return i
    return -1

print(numNotPresent([99,1,2,3,4],[2,3,99,1,4]))
