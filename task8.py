import math

def hypotenuse_Pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Задаємо довжини сторін a та b прямокутного трикутника
a = 133
b = 72

# Обчислення довжини гіпотенузи
c = hypotenuse_Pythagoras(a, b)

print("Довжина гіпотенузи прямокутного трикутника зі сторонами a={} і b={} дорівнює {:.2f}".format(a, b, c))
