def fibs(limit):
    a, b, res = 2, 3, []
    while a <= limit:
        res.append(a)
        a, b = b, a + b
    return res

FIB = fibs(10 ** 36)
print(FIB)

from functools import cache


# The cache decorator is used to memoize the results of function calls, which can significantly improve performance by avoiding redundant computations.
@cache
def fib_prod(n: int, m: int = 1) -> int:
    return 1 if n == 1 else sum(fib_prod(n // d, d) for d in FIB if d >= m and n % d == 0)
    
print(fib_prod(48))