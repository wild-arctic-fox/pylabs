import math

# Задані значення a і b
a = 10
b = 1

# Обчислюємо корені
x1 = math.sqrt(b / a)
x2 = -math.sqrt(b / a)

# Перевірка рівняння
result1 = a * x1**2 - b
result2 = a * x2**2 - b

print("Корінь x1:", x1)
print("Корінь x2:", x2)
print("Результат першої підстановки (a*x1^2 - b):", result1)
print("Результат другої підстановки (a*x2^2 - b):", result2)
