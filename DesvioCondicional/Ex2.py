"""
    DESVIO CONDICIONAL Composto
Se a idade for maior ou igual a 18, apresentar a mensagem
"você é maior de idade."
caso contrário, apresentar a mensagem "Você é menor de idade"
Data: 15/02/2025
Criado por: Pedro Veloso
Professora: Luciana
"""

idade = int(input("Digite sua idade: "))

#SE IDADE FOR MAIOR OU IGUAL A 18 FAÇA
if idade >= 18:
    #SE O TESTE LÓGICO FOR VERDADEIRO APRESENTA A LINHA ABAIXO
    print("Você é maior de idade")
else: # SENÃO
    #SE O TESTE LÓGICO FOR FALSO, APRESENTA A LINHA ABAIXO
    print("Você é menor de idade")

"""
    SINTAXE DA FUNÇÃO IF-ELSE
if teste_lógico:
    instrução_se_verdadeira
else:
    intrução_se_falsa
"""