import random

# Definindo o intervalo e a quantidade de números a sortear
NUMERO_MINIMO = 1
NUMERO_MAXIMO = 20
QUANTIDADE_SORTEAR = 10

# 1. Criar a lista completa de números possíveis (de 1 a 80)
numeros_possiveis = list(range(NUMERO_MINIMO, NUMERO_MAXIMO + 1))

# 2. Sortear (selecionar aleatoriamente) 20 números dessa lista, sem repetição
# O método 'sample' da biblioteca 'random' é perfeito para isso!
numeros_sorteados = random.sample(numeros_possiveis, QUANTIDADE_SORTEAR)

# 3. Opcional: ordenar os números para melhor visualização
numeros_sorteados.sort()

# 4. Exibir o resultado
print("-" * 35)
print(f"Sorteio de {QUANTIDADE_SORTEAR} números ÚNICOS de {NUMERO_MINIMO} a {NUMERO_MAXIMO}:")
print("-" * 35)
print(numeros_sorteados)
print("-" * 35)