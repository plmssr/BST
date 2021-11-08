def findMax(li, max):
    if li == []:
        return max
    else:
        if max <= li[0]:
            max = li[0]
        li = li[1:]
        return findMax(li, max)


li = [int(x) for x in input("enter list : ").split()]
print(findMax(li, li[0]))
