from random import randint


num1 = randint(1,100)
contador = 0
while True:
    num1 = randint(1, 100)
    contador = 0


    num2 = int(input("Digite um número de 1 à 100: "))

    if num2 != int:
        print("Apenas números inteiros são aceitos\n------------TENTE NOVAMENTE------------")
    else:

        if num2 > num1:
            contador = contador + 1
            print("O número é menor!")
        elif num2 < num1:
            contador = contador + 1
            print("O número é maior!")
        elif num2 == num1:
            print("Parábens você acertou!!")
            print("tentativas: ",contador)
            ops = int(input("Se deseja tentar denovo aperte [0] e se quiser sair aperte [1]"))
            if ops == 0:
                print("-------------------RECARREGANDO-------------------")
            else:
                print("Até a proxima S2 ;) !!")
                break


#by GPT
"""
from random import randint

while True:
    num1 = randint(1, 100)  # Gera um número aleatório
    contador = 0  

    while True:
        try:
            num2 = int(input("Digite um número de 1 a 100: "))
        except ValueError:
            print("Erro! Apenas números inteiros são aceitos.\n------------TENTE NOVAMENTE------------")
            continue

        contador += 1  # Conta a tentativa
        
        if num2 > num1:
            print("O número é menor!")
        elif num2 < num1:
            print("O número é maior!")
        else:
            print(f"Parabéns, você acertou!!\nTentativas: {contador}")
            break  

    # Opção de jogar novamente
    while True:
        ops = input("Deseja jogar novamente? [s/n]: ").strip().lower()
        if ops in ["s", "n"]:
            break
        print("Entrada inválida! Digite 's' para sim ou 'n' para não.")

    if ops == "n":
        print("Até a próxima S2 ;) !!")
        break
    else:
        print("-------------------RECARREGANDO-------------------")
"""










