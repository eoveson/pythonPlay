import collections

def permutations(word):
    if len(word) <=1:
        return [word]

    # get all permutations of length N-1
    perms = permutations(word[1:])
    char = word[0]
    result = set()
    # iterate over all permutations of length N-1
    for perm in perms:
        # insert the character into every possible location
        for i in range(len(perm) + 1):
            result.add(perm[:i] + char + perm[i:])
    return result

#print(permutations("NANA"))

def perms2(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack)!=0:
        c=stack.pop();
        results2 = []
        for w in results:
            for i in range(len(w)+1):
                results2.append(w[:i] + c + w[i:])
        results = results2
perms2("LSE")