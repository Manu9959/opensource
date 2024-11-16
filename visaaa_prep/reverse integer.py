def reverse_integer(n):
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    negative = n < 0
    n = abs(n)
    reverse_n = int(str(n)[::-1])
    if negative:
        reverse_n = -reverse_n
    if reverse_n < INT_MIN or reverse_n > INT_MAX:
        return 0
    return reverse_n
n = int(input())
print(reverse_integer(n))
