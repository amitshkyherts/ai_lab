#! /usr/bin/python3

# ---- assignment 0.5 ----
# 1.
print([i for i in range(2, 21) if i % 2 == 0])

# 2.
print([(x, x * x) for x in range(1, 11)])

# 3. numbers that divide 36
print([i for i in range(1, 37) if 36 % i == 0])

# 4.
print([
    (i, j)
    for i in range(1, 11)
    for j in range(1, 11)
    if i + j <= 50 and (i % j == 0 or j % i == 0)
])

# 5.
mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
print([i for i in mylist if i != 3 or i != 3.0])


# ---- assignment 0.7 ----
def triple_yield():
    yield 1
    yield 2
    yield 3


print(triple_yield())
print(triple_yield().__next__())
for i in triple_yield():
    print(i)


def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci series:")
for i in fib(8):
    print(i)

