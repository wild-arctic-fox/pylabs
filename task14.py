def count_lines_ending_with_symbol(filename, symbol):
    count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip().endswith(symbol):
                    count += 1

        return count

    except FileNotFoundError:
        return None

file_path = "file.txt"
ending_symbol = "어"

result = count_lines_ending_with_symbol(file_path, ending_symbol)

if result is not None:
    print(f"Кількість рядків, які закінчуються на '{ending_symbol}': {result}")
else:
    print("Файл не знайдено.")
