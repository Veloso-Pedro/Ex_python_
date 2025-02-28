"""
Faça um programa que pergunte a idade do usuário e informe se ele pode ou não se aposentar.
Obs. Uma pessoa só pode se aposentar quando atingir 60 anos (idade mínima).
Data: 15/02
Criado por: Pedro Veloso
Professora: Luciana
"""
idade = int(input("Digite sua Idade: "))

if idade >= 60:
    print("Você pode se aposentar")
else:
    print("Infelizmente, você ainda não pode se aposentar.")
