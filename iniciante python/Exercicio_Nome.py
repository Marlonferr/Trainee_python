nome = input('Qual o seu nome?')
nomee = nome[::-1]
idade = input('qual a sua idade')
nome_l = len(nome)

print("Seu nome é {nome}".format(nome = nome))
print("Seu nome invertido é: {nomee}".format(nomee = nomee))
print("sua idade é {idade}".format(idade = idade))



if  "" in nome and idade:
	print('há valores faltantes...')

print(f'seu nome tem {nome_l} letras')
print(f'A primeira letra do seu nome é {nome[:1:]}')
print(f'A primeira letra do seu nome é {nome[-1::]}')
if " " in nome:
	print('seu nome tem espaço')

else:
	print('não tem espaços')