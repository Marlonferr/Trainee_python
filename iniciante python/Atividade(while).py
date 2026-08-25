senha = input('digite uma senha para salvar: ')
repeticoes = 0

while True: 
    
    if  senha:
        print('senha salva')
    else:
        print('senha invalida')
        continue 
    i = input('digite a sua senha salva para entrar no programa: ')
   
    if i == senha: 
        print('acesso concedido ao programa')
        import subprocess
        subprocess.run(["Explorer"], check=True)
        break
       
    else:
        
        print('acesso negado',repeticoes)
        repeticoes += 1
        if repeticoes > 3:
            print('excedeu o limite de tentativas')
           
            break
    



 
   