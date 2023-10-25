quote = "Have you ever considered that you ask too much?"

# Ініціалізуємо порожній словник для збереження символів та їх кількості
char_count = {}

# Перебираємо кожен символ у цитаті
for char in quote:
    # Додаємо символ до словника або збільшуємо кількість, якщо символ вже є в словнику
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Виводимо усі унікальні символи та їх кількість
for char, count in char_count.items():
    print(f"'{char}': {count}")
