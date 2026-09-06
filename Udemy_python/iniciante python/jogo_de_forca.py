jogo = ['m','a','ç','a']          # Palavra a ser advinhada ("maçã")
jogotamp = ['*','*','*','*']      # Representação mascarada

while '*' in jogotamp:  # Enquanto houver letras não descobertas
    print("\nPalavra:", ' '.join(jogotamp))  # Mostra o progresso
    
    letra = input('\nDigite uma letra: ').lower()  # Recebe a letra
    
    # Verifica se a letra está na palavra
    for i in range(len(jogo)):
        if jogo[i] == letra:
            jogotamp[i] = letra  # Revela a letra correta

    # Mostra a palavra secreta (opcional, para debug)
    # print(jogo) 

print("\nParabéns! Você acertou a palavra:", ''.join(jogo))