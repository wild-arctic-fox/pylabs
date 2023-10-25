# Сума
sum = 0

start = 1
N = int(input("Введіть кількість цілих чисел для суми: "))

# Перебір
for i in range(start, N+1):
    sum += i*(i+1)/2

print("Сума:", sum)