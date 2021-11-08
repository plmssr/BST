def print_space(space):

    # base case
    if (space == 0):
        return
    print("^", end="")

    # recursively calling print_space()
    print_space(space - 1)

# function to print asterisks


def print_asterisk(asterisk):

    # base case
    if(asterisk == 0):
        return
    print("#", end="")

    # recursively calling asterisk()
    print_asterisk(asterisk - 1)

# function to print the pattern


def pattern(n, num):

    # base case
    if (n == 0):
        return
    print_space(n - 1)
    print_asterisk(2*(num - n + 1)-1)
    print_space(n-1)
    print("")

    # recursively calling pattern()
    pattern(n - 1, num)


# Driver Code
n = int(input("Enter Input : "))
if n <= 0:
    print('Not Draw!')
else:
    pattern(n, n)
