palavra = str(input("Digite uma palavra ou frase: ")).lower().replace(" ", "")
vogais ='aeiou'
count = 0

for letras in palavra:
    if letras in vogais:
        continue
    else:
        count += 1

print(f"Quantidade de Cosoantes é igual a {count}")