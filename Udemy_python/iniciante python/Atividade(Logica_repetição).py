nome = input("Qual o seu nome? ").lower()
p = "*"
contador = 0
while True:
    print(p,end="")
    print(nome[contador], end="")
    print(p,end="")
    contador += 1 
    if contador == len(nome):
        break