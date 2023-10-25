# Задана послідовність гена PalB2 у форматі ДНК
gene_sequence_dna = """
CTGTCTCCCTCACTGTATGTAAATTGCATCTAGAATAGCA
TCTGGAGCACTAATTGACACATAGTGGGTATCAATTATTA
TTCCAGGTACTAGAGATACCTGGACCATTAACGGATAAAT
AGAAGATTCATTTGTTGAGTGACTGAGGATGGCAGTTCCT
GCTACCTTCAAGGATCTGGATGATGGGGAGAAACAGAGAA
CATAGTGTGAGAATACTGTGGTAAGGAAAGTACAGAGGAC
TGGTAGAGTGTCTAACCTAGATTTGGAGAAGGACCTAGAA
GTCTATCCCAGGGAAATAAAAATCTAAGCTAAGGTTTGAG
GAATCAGTAGGAATTGGCAAAGGAAGGACATGTTCCAGAT
GATAGGAACAGGTTATGCAAAGATCCTGAAATGGTCAGAG
CTTGGTGCTTTTTGAGAACCAAAAGTAGATTGTTATGGAC
CAGTGCTACTCCCTGCCTCTTGCCAAGGGACCCCGCCAAG
CACTGCATCCCTTCCCTCTGACTCCACCTTTCCACTTGCC
CAGTATTGTTGGTGT
"""

# Замінюємо T на U, щоб отримати послідовність мРНК
gene_sequence_mrna = gene_sequence_dna.replace("T", "U")

# Видаляємо символи нового рядка для підрахунку загальної довжини
gene_sequence_mrna = gene_sequence_mrna.replace("\n", "")

# Підраховуємо кількість урацилів та загальну довжину послідовності мРНК
uracil_count = gene_sequence_mrna.count("U")
total_length = len(gene_sequence_mrna)

# Виводимо результат
print("Кількість урацилів (U) у послідовності: ", uracil_count)
print("Загальна довжина послідовності мРНК: ", total_length)
