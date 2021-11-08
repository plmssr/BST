def palindrome(li):
    if len(li) < 2:
        return True
    else:
        if li[:1] == li[-1:]:
            return palindrome(li[1:-1])
        else:
            return False


s = 'Are we not drawn onward, we few, drawn onward to new era'
s = s.replace(' ', '')
s = s.lower()
print(s)
print(palindrome(list(s)))
