import numpy as np


def cuadrado_magico(num):
    matriz = np.zeros((num, num))
    matriz[0, num // 2] = 1  # Paso 1
    a = 0
    b = num // 2
    for i in range(2, num ** 2 + 1):
        if (i - 1) % num == 0:  # Paso 4
            a += 1
            if a > num - 1:
                a = 0
        else:  # Paso 2
            if a - 1 < 0:
                a = num - 1
            else:
                a -= 1
            if b + 1 == num:
                b = 0
            else:
                b += 1
        matriz[a, b] = i
    print(matriz)


num = int(input("Ingresa un número impar: "))
while num % 2 == 0:
    print("No es un número impar")
    num = int(input("Ingresa un número impar: "))
else:
    cuadrado_magico(num)
