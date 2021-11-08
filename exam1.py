def sum(num):
    if num == 1:
        print(str(num), end=' ')
        return num
    else:
        ans = 1/num+sum(num-1)
        print(str(num), end=' ')
        return ans


inp = int(input("Enter number : "))
print("=%.8f" % (sum(inp)))
