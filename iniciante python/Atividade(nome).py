nome = input("Qual é a primeira letra do seu nome?")
nome2 = len(nome)
if nome2 <= 5:
	print("seu nome é muito curto")
elif nome2 > 5 and nome2 < 10:
	print("Seu nome é Normal")
else:
	print("Seu nome é muito longo")