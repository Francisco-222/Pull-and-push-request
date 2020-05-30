def lone_sum(a, b, c):
    if a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return a+b+c

----------
-------
def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return c
    elif a >= b:
        return b
    elif b == c:
        return a
    elif a == c:
        return b
    else:
        print(lone_sum(3, 5, 7)
