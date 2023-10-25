def is_natural_number(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    else:
        return is_natural_number(n - 1)

n = 109
result = is_natural_number(n)
if result:
    print(f"{n} є натуральним числом.")
else:
    print(f"{n} не є натуральним числом.")
