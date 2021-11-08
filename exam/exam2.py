def findMax(li, max):
    if li == []:
        return max
    else:
        if li[0] >= max:
            max = li[0]
        return findMax(li[1:], max)


inp = [int(x) for x in input("Enter Input : ").split()]
print('Max :', findMax(inp, inp[0]))
