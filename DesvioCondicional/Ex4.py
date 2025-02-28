"""
    DESVIO CONDICIONAL ANINHADO (ENCADEADO) - IF-ELIF-ELSE
Verifique se o número digitado é positivo, negativo ou igual a zero.
Data: 15/02/2025
Criado por: Pedro Veloso
Professora: Luciana
"""
num1 = int(input("Digite um número: "))

if num1 > 0:
    print("Seu número é positivo!")
elif num1 < 0:
    print("Seu número é negativo")
else:
    print("Seu número é zero")

"""
    SINTAXE IF-ELFI-ELSE
if teste_lógico1:
    intrução_se_verdadeira1
elif teste_lógico2:
    intrução_se_verdaeira2
else:
    intrução_se_falsa 
"""