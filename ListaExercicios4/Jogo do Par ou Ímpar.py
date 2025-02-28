"""
Desafio: Jogo do Par ou Ímpar 🎲
Crie um programa em Python que:

Peça ao usuário para escolher Par ou Ímpar.
Peça ao usuário para inserir um número inteiro.
O computador também escolhe um número aleatório entre 1 e 10.
A soma dos dois números é calculada.
O programa verifica se a soma é par ou ímpar e informa quem ganhou.
O jogo deve continuar até o usuário decidir parar.
Bônus (Se quiser um desafio extra) 🔥
✅ Verifique se a entrada do usuário é válida (se escolheu "Par" ou "Ímpar" corretamente e digitou um número inteiro).
✅ Conte quantas rodadas o usuário venceu antes de perder.
✅ No final, exiba a quantidade total de vitórias consecutivas do usuário.
"""



from random import randint

while True:
    num1 = randint(1,10)
    ops = input("Escolha par ou impar")
    if ops == "par":
        try:
            num2 = int(input("Escolha um número par: "))
        except ValueError:
            print("Apenas números inteiros serão aceitos!!")
            continue
            total = num1 + num2

    else:
        try:
            num2 = int(input("Escolha um número impár: "))
        except ValueError:
            print("Apenas números inteiros serão aceitos!!")
            continue




