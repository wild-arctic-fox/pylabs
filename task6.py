# Задана послідовність
sequence = "AATGATACGGCGACCACCGAGATCTACACGCCTCCCTCGCGC" \
           "CATCAGAGAGTCTGGGTCTCAGGTACCGCAGTTGTATCTTGCGCGACTATA" \
           "ATCCACGGCTCTTATTCTAGCGTGCGCGTACGGCGGTGGGCGTCGTTACGCTATATT"

# Швидкість читання (припустимо, 1000 символів на секунду)
reading_speed = 1000  # символів на секунду

# Розрахунок тривалості читання
reading_time = len(sequence) / reading_speed

# Виведемо результат
print("Тривалість читання:", reading_time, "секунд")

# Підрахунок кількості G, C, A та T у послідовності
g_count = sequence.count('G')
c_count = sequence.count('C')
a_count = sequence.count('A')
t_count = sequence.count('T')

# Обчислення GC-вмісту
gc_content = ((g_count + c_count) / (a_count + t_count + c_count + g_count)) * 100

# Виведемо результат
print("GC-вміст прочитаного:", gc_content, "%")

# Адаптер Nextera
adapter = "AATGATACGGCGACCACCGAGATCTACACGCCTCCCTCGCGCCATCAG"

# Швидкість читання (припустимо, 1000 символів на секунду)
reading_speed = 1000  # символів на секунду

# Пошук адаптера в послідовності
adapter_position = sequence.find(adapter)

if adapter_position != -1:
    # Адаптер знайдено
    print("Адаптер Nextera присутній в прочитаному.")

    # Розрахунок тривалості читання до початку адаптера
    reading_time = adapter_position / reading_speed
    print("Тривалість читання до адаптера:", reading_time, "секунд")
else:
    # Адаптер не знайдено
    print("Адаптер Nextera відсутній в прочитаному.")