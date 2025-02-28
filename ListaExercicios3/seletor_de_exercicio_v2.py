
def ex1():
    import L3E1

def ex2():
    import L3E2

def ex3():
    import L3E3

def ex4():
    import L3E4

def ex5():
    import L3E5

while True:
    esc0 =input("Escolha o número do exercício 1, 2, 3, 4, 5 ou 0 caso queira sair: ")

    if esc0 == "1":
        ex1()
    elif esc0 == "2":
        ex2()
    elif esc0 == "3":
        ex3()
    elif esc0 == "4":
        ex4()
    elif esc0 == "5":
        ex5()
    elif esc0 == "0":
        print("Obrigado por testar!!")
        break
    else:
        print("O exercício selecionado n existe!!")
