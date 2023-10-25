def count_words_and_characters(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            character_count = len(content)
        return word_count, character_count
    except FileNotFoundError:
        return None

file_path = 'example.txt'

result = count_words_and_characters(file_path)
if result is not None:
    word_count, character_count = result
    print(f"Кількість слів: {word_count}")
    print(f"Кількість символів: {character_count}")
else:
    print("Файл не знайдено.")
