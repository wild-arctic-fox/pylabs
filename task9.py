sequence = []
number = int(input("Введіть число (завершити введення 0): "))

while number != 0:
    sequence.append(number)
    number = int(input("Введіть наступне число (завершити введення 0): "))

if sequence:
    for num in reversed(sequence):
        print(num)
else:
    print("Не введено жодного числа.")

