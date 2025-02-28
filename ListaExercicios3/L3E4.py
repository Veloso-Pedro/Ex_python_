"""
Escreva um programa que solicite ao usuário dois números e exiba a soma, subtração,
multiplicação e divisão entre eles. Utilize o tipo de dados double.
Data: 15/02/2025
Criado por: Pedro Veloso
Professora: Luciana
"""
num1 = float(input("Digite um número: "))
num2 = float (input("Digite outro número: "))
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"A soma é {soma:.2f}, A subtração é {sub:.2f}, a multiplicação é {mult:.2f}, divisão é {div:.2f}")