import collections

def fib(n):
    a,b = 0,1
    results = [a, b]
    for i in range(n):
        a,b = b, a+b
        results.append(b)
    print(results)

def fib2(n, hash):
    if n < 2:
        hash[n]=n
        return n
    hash[n]=fib2(n-1,hash)+fib2(n-2,hash)
    return hash[n]

def selSort(result):
    for i in range(len(result)):
        k=i
        for j in range(k+1, len(result)):
            if result[j] < result[k]:
                k = j

        result[i], result[k] = result[k], result[i]

arr = [2, 5, 99, -1, 1, 9, 8, 3]
selSort(arr)
print(arr)

#hash1 = collections.defaultdict(int)
#print(fib2(7, hash1))
#for value in hash1.values():
#    print(value)