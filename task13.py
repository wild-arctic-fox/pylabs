import string

with open("output.txt", "w", encoding="utf-8") as file:
    for i, letter in enumerate(string.ascii_lowercase[:9], start=1):
        line = letter * i
        file.write(line + "\n")
