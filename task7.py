import random

# Випадково вибираємо позицію в межах 1 до 5202
position = random.randint(1, 5202)

# Граничні позиції генів A та B
start_gene_A = 1000
end_gene_A = 3400
start_gene_B = 3700
end_gene_B = 6000

# Перевірка умов
is_in_gene_A = start_gene_A <= position <= end_gene_A
is_in_gene_B = start_gene_B <= position <= end_gene_B
is_between_genes = end_gene_A < position < start_gene_B
is_in_either_gene = is_in_gene_A or is_in_gene_B
is_outside_both_genes = not is_in_gene_A and not is_in_gene_B
is_in_range_100_to_start_A = 100 <= position < start_gene_A

# Виведення результатів
print("Позиція в гені A:", is_in_gene_A)
print("Позиція в гені B:", is_in_gene_B)
print("Позиція між двома генами:", is_between_genes)
print("Позиція в одному з двох генів:", is_in_either_gene)
print("Позиція поза обома генами:", is_outside_both_genes)
print("Позиція в межах 100 до початку гена А:", is_in_range_100_to_start_A)
