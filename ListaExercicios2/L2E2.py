"""
Calcular o perímetro do círculo
Data: 15/02/2025
Criado por: Pedro Veloso
Professora: Luciana
"""

import math
from math import pi

raio = "raio"
diametro = "diametro"


esc = input(f"Escolha {raio} ou {diametro} : ")

if esc == raio:
    num2 = float(input("Digite o valor do Raio: "))
    circ2 = 2 * pi * num2

    print(f"Usando o raio para calcular o perimetro o resultado é :{circ2:.4}")

else:
    num1 = float(input("Digite o Valor do Diametro: "))
    circ = num1 * pi

    print(f"O perímetro é igual a {circ:.4}")



