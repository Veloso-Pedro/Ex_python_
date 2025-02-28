"""
nome = 'Gaspar'
sobrenome = 'Ricardo'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)
"""

import random
from random import randint

sorte = random.randint(1,10)

num = int(input('Escolha um numero de 1 a 10:'))

if num == sorte :
    print('VOCÊ GANHOU PARÁBENS!! \n o Numero sorteado foi', sorte)
else:
    print('VOCÊ PERDEU :( \n o Numero Sorteado foi', sorte)