def SelSort(ary, i):
    if i == len(ary): return
    curMin = i
    for j in range(i+1, len(ary)):
        if ary[j] < ary[curMin]:
            curMin = j
    ary[i], ary[curMin] = ary[curMin], ary[i]
    SelSort(ary, i+1)

ary = [15, 3, 2, 9, 1, 5]
SelSort(ary, 0)
print(ary)