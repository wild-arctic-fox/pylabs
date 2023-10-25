# Задана послідовність
chain_a = """SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKM
FCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVV
RRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFR
HSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILT
IITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKG
EPHHELPPGSTKRALPNNT"""

# Знаходимо перший рядок
first_line_start = 0
first_line_end = chain_a.find('\n')

# Витягуємо перший рядок
first_line = chain_a[first_line_start:first_line_end]

# Виводимо перший рядок
print(first_line)
