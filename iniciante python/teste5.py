# Solicita ao usuário que digite dois valores
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')

# Converte os valores para inteiros para realizar a comparação
primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

# Compara os valores e imprime o resultado
if primeiro_valor < segundo_valor:
    print('O', segundo_valor, 'é maior que o', primeiro_valor)
elif primeiro_valor > segundo_valor:
    print('O', primeiro_valor, 'é maior que o', segundo_valor)
else:
    print('Os valores adicionados são iguais')
