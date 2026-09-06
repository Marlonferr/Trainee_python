# Contadores globais
total_veiculos = 0
veiculos_isentos = 0

while True:
    def horario(a=8, b=18):
        x = b - a
        tempo = int(input('Quantas horas o cliente deseja ficar? '))
        if tempo <= x:
            print('Pode entrar no estacionamento.')
        else:
            print('Não é possível permanecer esse tempo no estacionamento.')

    def pagamento(total_horas):
        global veiculos_isentos
        if total_horas <= 1:
            print('Isento de pagamento.')
            veiculos_isentos += 1
        elif total_horas <= 2:
            valor = total_horas * 1.5
            print(f'Valor a ser pago: R${valor:.2f}')
        elif total_horas > 2:
            valor = (2 * 1.5) + ((total_horas - 2) * 1.0)
            print(f'Valor a ser pago: R${valor:.2f}')
        else:
            print('Erro no cálculo.')

    def saida(entrada):
        p = input('Quer sair do estacionamento? (sim/não) ').lower()
        if p == 'sim':
            hora_saida = int(input('Hora da saída? '))
            total_horas = hora_saida - entrada
            if total_horas < 0:
                print('Hora de saída inválida.')
                return
            print(f'Tempo total: {total_horas} hora(s).')
            pagamento(total_horas)
            print('Obrigado por usar nosso estacionamento!')
        elif p == 'não':
            print('Ok, aproveite o estacionamento!')
        else:
            print('Resposta inválida. Digite "sim" ou "não".')

    def relatorio():
        print(f'\n--- RELATÓRIO ---')
        print(f'Veículos no total: {total_veiculos}')
        print(f'Veículos isentos: {veiculos_isentos}')
        print('-----------------\n')

    entrada = int(input('Qual o horário de entrada do cliente? (apenas hora inteira, ex: 9) '))
    horario(a=entrada)

    print('Qual o seu veículo? (carro, moto, caminhonete)')
    perg1 = input().lower()

    if perg1 in ('carro', 'moto', 'caminhonete'):
        print('Veículo aceito!')
        total_veiculos += 1
    else:
        print('Veículo não aceito!')
        continue  # Volta pro início do loop se o veículo for inválido

    saida(entrada)
    relatorio()
