import datetime

i = input('quer saber a hora atual, [Sim] ou [Não]?')

if i == 'Sim' or 'sim':
    relogio = datetime.datetime.now()
    print(relogio)

else:
    print('ok, tenha um bom dia!')

