def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 13
result = fibonacci(n)
print(f"{n}-е число Фібоначчі дорівнює {result}")
