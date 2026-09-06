
def verificarnumero():
    numbi = input("Digite um número inteiro: ")
    if not numbi.isdigit():
        print("entrada invalida")
        return
    transf = int(numbi)
    
    aaa = transf % 2
    if aaa == 1:
            print("seu numero é impar")

    else:
        print("Seu numero é par")
verificarnumero()