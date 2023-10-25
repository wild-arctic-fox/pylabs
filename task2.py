def sum_numbers(*args):
    total = 0
    for number in args:
        if isinstance(number, (int, float)):
            total += number
        else:
            print(f"Попередження: Аргумент '{number}' не є числом і буде проігнорований.")
    return total

result = sum_numbers(233, 377, 610.0, "jane")
print("Сума чисел:", result)

