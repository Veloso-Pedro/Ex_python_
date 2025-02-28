"""
    DESVIO CONDICIONAL ANINHADO (ENCADEADO)
Verifique se o número digitado é positivo, negativo ou igual a zero.
Data: 15/02/2025
Criado por: Pedro Veloso
Professora: Luciana
"""

num1 = int(input("Digite um número: "))

if num1 > 0:
    print("Seu número é positivo!")

else:
    if num1 < 0:
        print("Seu número é negaivo!")
    else:
        print("Seu número é igual a zero!")

"""
    SINTAXE DO DESVIO CONDICIONAL ANINHADO
if teste_lóico1:
    instrução_se_verdadeira1
else:
    if teste_lógico2:
        intrução_se_verdadeiro2
    else:
        intrução_se_falsa2

"""