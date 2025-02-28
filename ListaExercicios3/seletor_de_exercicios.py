"""
while True:

    esc0 = input("Qual exercicio vc deseja ver 1, 2 ou 3: ")

    if esc0 == "1":
        a = float(input("A = "))
        b = float(input("B = "))
        c = float(input("C = "))
        delta = (b ** 2) - (4 * a * c)

        print(f"O Resultado de Delta é {delta:.2f}")

    elif esc0 == "2":
        larg = float(input("Digite a largura: "))
        comp = float(input("Digite o comprimento: "))
        per = 2 * (larg + comp)
        area = larg * comp

        print(f"A área é {area} e o Perímetro é {per}")

    elif esc0 == "3":
        from math import pi

        raio = float(input("Digite o raio: "))
        vol = (4 * pi * raio ** 3) / 3

        print(f"O volume da esfera é {vol:.2f} ")

    else:
        print("Erro!")
        break
"""
#by gpt
from math import pi

def calcular_delta():
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))
    delta = (b ** 2) - (4 * a * c)
    print(f"O Resultado de Delta é {delta:.2f}")

def calcular_area_perimetro():
    larg = float(input("Digite a largura: "))
    comp = float(input("Digite o comprimento: "))
    per = 2 * (larg + comp)
    area = larg * comp
    print(f"A área é {area} e o Perímetro é {per}")

def calcular_volume_esfera():
    raio = float(input("Digite o raio: "))
    vol = (4 * pi * raio ** 3) / 3
    print(f"O volume da esfera é {vol:.2f}")

while True:
    esc0 = input("Qual exercício você deseja ver? 1, 2, 3 ou 0 para sair: ")

    if esc0 == "1":
        calcular_delta()
    elif esc0 == "2":
        calcular_area_perimetro()
    elif esc0 == "3":
        calcular_volume_esfera()
    elif esc0 == "0":
        print("Saindo do programa...")
        break
    else:
        print("Erro! Opção inválida.")


