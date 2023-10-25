def count_classes_and_subjects(filename):
    subjects = set()
    lecture_count = 0
    lab_count = 0
    practical_count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split(': ')
                if len(parts) == 2:
                    subjects.update(parts[1].strip().split(', '))

            for subject in subjects:
                if 'лекція' in subject:
                    lecture_count += 1
                if 'лабораторна' in subject:
                    lab_count += 1
                if 'практична' in subject:
                    practical_count += 1

        return len(subjects), lecture_count, lab_count, practical_count

    except FileNotFoundError:
        return None

file_path = 'schedule.txt'

result = count_classes_and_subjects(file_path)
if result is not None:
    total_subjects, lectures, labs, practicals = result
    print(f"Кількість різних предметів: {total_subjects}")
    print(f"Кількість лекцій: {lectures}")
    print(f"Кількість лабораторних занять: {labs}")
    print(f"Кількість практичних занять: {practicals}")
else:
    print("Файл не знайдено.")
