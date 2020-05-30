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
scenario 1:
Let us assume a=12,b=9 c=4
if a>=b true so we will return c which is 4

scenario 2:
Let us assume a=8,b=9 c=4
if a>=b false
a==c false
b==c false
a==b and a==c and b==c false
so we will return a+b+c which is 21
