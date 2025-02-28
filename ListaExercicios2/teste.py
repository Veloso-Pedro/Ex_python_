# by me
from math import pi

def calcula_area_circulo_r():
        num1 = float(input("Dite o Raio: "))
        area = pi * num1 ** 2
        print(f"A área da circunferencia é {area:.4f}")

def calcula_perimetro_circulo_r():
        num2 = float(input("Digite o valor do Raio: "))
        circ2 = 2 * pi * num2
        print(f"Usando o raio para calcular o perimetro o resultado é :{circ2:.4}")

def calcula_perimetro_circulo_d():
    num1 = float(input("Digite o Valor do Diametro: "))
    circ = num1 * pi
    print(f"O perímetro é igual a {circ:.4}")



esc0 = int(input(print(f"Você quer calcular 1 -area ou 2- perimetro da circunferencia?")))


if esc0 == 1:
    calcula_area_circulo_r()
else:
    raio = "raio"
    diametro = "diametro"

    esc = input(f"Escolha {raio} ou {diametro} : ")

    if esc == raio:
        calcula_perimetro_circulo_r()
    else:
        calcula_perimetro_circulo_d()


"""
#by chatgpt
from math import pi

# Pergunta ao usuário se ele quer calcular área ou perímetro
esc0 = int(input("Você quer calcular 1 - área ou 2 - perímetro da circunferência? "))

# Se for para calcular a área
if esc0 == 1:
    raio = float(input("Digite o Raio: "))
    area = pi * raio ** 2
    print(f"A área da circunferência é {area:.4f}")

# Se for para calcular o perímetro
else:
    escolha = input("Escolha 'raio' ou 'diametro' para calcular o perímetro: ").strip().lower()

    if escolha == 'raio':
        raio = float(input("Digite o valor do Raio: "))
        perimetro = 2 * pi * raio
        print(f"Usando o raio para calcular o perímetro, o resultado é: {perimetro:.4f}")

    elif escolha == 'diametro':
        diametro = float(input("Digite o valor do Diâmetro: "))
        perimetro = pi * diametro
        print(f"O perímetro usando o diâmetro é: {perimetro:.4f}")

    else:
        print("Escolha inválida! Você deve escolher 'raio' ou 'diametro'.")
        
"""