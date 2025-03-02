palavra = str(input("Digite uma palavra ou frase: ")).lower()
vogais ='aeiou'
count = 0

for letras in palavra:
    if letras in vogais:
        count += 1

print(f"Quantidade de vogais igual á {count}")







