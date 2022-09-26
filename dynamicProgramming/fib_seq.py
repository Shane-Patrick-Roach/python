
def fib(n, map = {}):
    if n in map:
        return map[n]
    if n <= 2:
        return 1
    map[n] = fib(n - 1) + fib(n - 2)
    return map[n]


print(fib(6))
print(fib(59))
print(fib(100))