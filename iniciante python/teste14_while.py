while True:
    print('É uma fruta')
    palavra = input('Digite a palavra certa: ')
    
    if palavra.lower() != 'pera': #!= sinal de diferente.
        print('Palavra errada.')
    else:
        print('Você acertou!')
        break
    