"""
    DESVIO CONDICIONAL SIMPLES
Apresenta a mensagem se o número inteiro digitado for mair que 1000.
Data: 15/02/2025
Criado por: Pedro Veloso
Professora: Luciana
"""
#ENTRADA
num1 = int(input("Digite um numero inteiro"))

#SE O NÚMERO FOR MAIOR QUE 1000 FAÇA
if num1 > 1000:
    print("O número digitado é maior que 1000") #MENSAGEM SE VERDADEIRO

#APRESENTA AMENSAGEM INDEPENDENTE DO IF, PORQUE ESTÁ NO MESMO NÍVEL DO IF
print("Fim...")

"""
SINTAXE DA FUNÇÃO IF SIMPLES

if teste_logico:
    linha_instrução_se_verdadeiro
    
"""
