# Задана послідовність та інформація про SNP
sequence = "CATTATTTTCACTTGGGTCGAGGCCAGATTCCATC[G/A]GGATTGCCCGAAATCAGAGAAAAGTCG"
iupac_snp = "R"

# Знаходимо позицію початку SNP у регіоні
start_snp = sequence.find("[G/A]")

if start_snp != -1:
    # Витягуємо та надрукуємо SNP та його нотацію IUPAC
    snp = sequence[start_snp:start_snp + 5]  # Включно з "[G/A]"
    iupac_region = iupac_snp
    print("SNP з регіону:", snp)
    print("IUPAC_region:", iupac_region)
else:
    print("SNP не знайдено у регіоні.")
