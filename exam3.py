def gcd(a, b):
    if a == b == 0:
        return 'value = 0'
    else:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)


inp = [int(x) for x in input("enter 2 int : ").split()]

print(gcd(inp[0], inp[1]))
