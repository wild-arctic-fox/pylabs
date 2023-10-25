def power(base, exponent):
    result = 1
    if exponent >= 0:
        for _ in range(exponent):
            result *= base
    else:
        for _ in range(-exponent):
            result /= base
    return result

base = 87216387
exponent = -4
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
