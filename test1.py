def sum(data):
    # base case
    if data == 1:
        print(data, end='')
        return data
    # recursion
    else:
        ans = data+sum(data-1)
        print(f'+{data}', end='')
        return ans


x = sum(10)
print('')
print(x)
