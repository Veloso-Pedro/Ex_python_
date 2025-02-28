"""
Exempl de média com formatação na saída
Data 15/02/2025
Criado por : Pedro Veloso
Professpra : Luciana
"""
# ENTRADA - Solicita para o usuário digitar as notas
nota1 = float(input("Digite a priemira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 =  float(input("Digite a terceira nota: "))

# PROCESSAMENTO - Calcula a média aritmética
media = (nota1 + nota2 + nota3)/ 3.0
# SAÍDA - Exibe a média formatada
print(f"A Média entre {nota1} + {nota2} + {nota3} é {media:.2}")