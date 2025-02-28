"""
Escreva um programa que calcule o delta de uma equação de segundo grau.
criado por: Pedro Veloso
Data 15/02/2025
Professora: Luciana
"""

#Fórmula: ∆ = b^2 − 4ac

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
delta = (b ** 2) - (4 * a * c)

print(f"O Resultado de Delta é {delta:.2f}")