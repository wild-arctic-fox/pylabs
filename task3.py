def build_table(func, values):
    table = {}
    for value in values:
        result = func(value)
        table[value] = result
    return table

# Приклад використання функції
def anyfunc(x):
    return x ** 3

values = [1, 2, 3, 4, 5]
table = build_table(anyfunc, values)
print(table)
