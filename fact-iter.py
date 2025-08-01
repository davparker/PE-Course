# Factorial using Iteration


def fact_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


print(fact_iter(4))

# Factorial using Recursion


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(4))
