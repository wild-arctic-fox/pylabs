# Введення послідовності праймера
primer_sequence = "TTAGCACACGTGAGCCAATGGAGCAAACGGGTAATT"

# Знаходимо кількість G і C (GC) у послідовності
gc_count = primer_sequence.count("G") + primer_sequence.count("C")

# Знаходимо довжину праймера (N)
primer_length = len(primer_sequence)

# Обчислюємо температуру плавлення (Tm) за формулою
Tm = 64.9 + (41 * (gc_count - 16.4)) / primer_length

# Виводимо результат
print("Температура плавлення Tm праймера: {:.2f} градусів Цельсія".format(Tm))
