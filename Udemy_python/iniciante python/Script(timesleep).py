import time #importa a hora atual da biblioteca python atualizado
from datetime import datetime #para todo datatime importa a hora

def gera():
    for conti in range(1, 6):
        mensagem = f"Pensando... {conti}"
        
        for letra in mensagem:
            print(letra, end='', flush=True)
            time.sleep(0.1)
        
        print()
        time.sleep(0.5)

def hor():
    perg = input("Qual a hora atual? ")
    
    if not perg.isdigit():
        print("Entrada inválida!")
        return
    
    hora = int(perg)
    
    gera()  # aparece o "Pensando..." antes da resposta
    
    if hora < 12:
        print(f"Bom dia! São {hora}:00")
    elif hora < 18:
        print(f"Boa tarde! São {hora}:00")
    else:
        print(f"Boa noite! São {hora}:00")

hor()