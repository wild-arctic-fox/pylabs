def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = 8
result = factorial(n)
print(f"Факторіал числа {n} дорівнює {result}")
