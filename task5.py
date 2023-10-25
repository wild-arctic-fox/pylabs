def calculate_expression(x, n):
    result = 0
    expression = ""

    for i in range(n + 1):
        term = x**i
        result += term
        if i > 0:
            expression += f" + {x}^{i}"
        else:
            expression += f"1"

    return result, expression

x = 2
n = 5

result, expression = calculate_expression(x, n)
print(f"{expression} = {result}")

