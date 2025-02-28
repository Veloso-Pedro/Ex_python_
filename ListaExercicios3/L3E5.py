"""
Escreva um programa que calcule a média geométrica entre três números informados pelo
usuário. Utilize o tipo de dados double.
Data: 15/02/2025
Criado por: Pedro Veloso
Professora: Luciana
"""
from math import cbrt

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
mg = cbrt(num1*num2*num3)

print(f"A Média Geométrica é {mg:.6f}")