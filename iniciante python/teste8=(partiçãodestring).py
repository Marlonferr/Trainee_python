nome = input('digite o seu nome!')
idade = input('digite sua idade!')
if nome and idade:
    print('O seu nome é',nome,'e sua idade é',idade,'anos')
    print('seu nome ao contrário', nome[::-1])
    print('A quantidade de carácteres do seu nome é', len(nome))
    print('A primeira letra do seu nome é',nome[0])
    print('A última letra do seu nome é',nome[5])
else:
    print(' você deixou campos vazios!')

if ' ' in nome:
    print('seu nome contém espaços!')

else:
    print('')