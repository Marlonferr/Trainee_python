while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, *, /): ')

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except ValueError:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if operador == '+':
        resultado = num_1_float + num_2_float
    elif operador == '-':
        resultado = num_1_float - num_2_float
    elif operador == '*':
        resultado = num_1_float * num_2_float
    elif operador == '/':
        if num_2_float == 0:
            print('Erro: Divisão por zero!')
            continue
        resultado = num_1_float / num_2_float

    print(f'O resultado de {num_1_float} {operador} {num_2_float} é {resultado}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break
