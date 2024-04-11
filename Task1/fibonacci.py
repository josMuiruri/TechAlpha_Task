def fib(limit):
    a, b = 0, 1
    while a <= limit:
        yield a

        a, b = b, a + b


limit = 99
fib_sequence = list(fib(limit))
print(fib_sequence)
