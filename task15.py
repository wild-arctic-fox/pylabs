def invert_lines_ending_with_symbol(filename, symbol):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip().endswith(symbol):
                    inverted_line = line[::-1]
                    print(inverted_line)

    except FileNotFoundError:
        print("Файл не знайдено.")

file_path = "pain.txt"
ending_symbol = "줘"

invert_lines_ending_with_symbol(file_path, ending_symbol)
