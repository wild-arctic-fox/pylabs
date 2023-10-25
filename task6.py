# Сума
sum = 0

start = 1
end = 1200

# Перебір
for i in range(start, end+1):
    sum += i*(i+1)/2

print("Сума:", sum)
