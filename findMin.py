def finMin(lst, min):
    if lst == []:
        return min
    else:
        if lst[0] <= min:
            min = lst[0]
        lst.pop(0)
        return finMin(lst, min)


li = [1, ]
print(finMin(li, li[0]))
