"""
Faça um programa que leia as notas de duas provas, calcule a média aritmética simples, e
informe se o aluno foi aprovado (média maior ou igual a 6) ou reprovado (média menor que 6).
Data: 15/02
Criado por: Pedro Veloso
Professora: Luciana
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

if media >= 6:
    print(f"Média: {media}\nStatus: Aprovado!!")
else:
    print(f"Média: {media}\nStatus: Reprovado :(")