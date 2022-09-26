def fib_while(n):
    a, b = 1, 1
    if n < 2:
        print(a, b)
        return
    count = 0
    while count < n - 2:
        a, b = b, a + b
        count += 1
        print(b)


def fib_for(n):
    a, b = 1, 1
    if n < 2:
        print(a, b)
        return
    for i in range(2, n):
        a, b = b, a + b
        print(b)


def fib_recursive(n):
    if n in [1, 2]:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


fib_while(10)
print("---------------")
fib_for(10)
print("---------------")
# this prints just the n-th number in the sequence
print(fib_recursive(10))
print("---------------")
