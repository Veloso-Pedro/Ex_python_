"""
Crie um programa que solicite ao usuário o valor do raio de uma esfera e calcule o seu volume.
criado por: Pedro Veloso
Data 15/02/2025
Professora: Luciana
"""
from math import pi
raio = float(input("Digite o raio: "))
vol = (4 * pi * raio ** 3) / 3

print(f"O volume da esfera é {vol:.2f} ")
