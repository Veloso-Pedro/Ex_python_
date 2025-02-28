palavra = input("Digite uma palavra ou frase: ").lower().replace(" ", "")
reverse = palavra[::-1]

if palavra == reverse:
    print("Essa é um palíndromo!!")
else:
    print("Essa palavra não é um palíndromo!!")
