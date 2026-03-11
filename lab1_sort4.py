def sort4(a, b, c, d):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if a > c:
        a, c = c, a
    if b > d:
        b, d = d, b
    if b > c:
        b, c = c, b
    return a, b, c, d


print(sort4(4, 2, 1, 3))
