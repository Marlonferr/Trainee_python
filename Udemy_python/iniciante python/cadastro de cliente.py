import json

def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def cadastrar_cliente(clientes):
    print("\n=== Cadastro de Cliente ===")
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cliente = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")

def listar_clientes(clientes):
    print("\n=== Lista de Clientes ===")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. Nome: {cliente['nome']}, Idade: {cliente['idade']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")
    print()

def main():
    arquivo = "clientes.json"
    clientes = carregar_dados(arquivo)

    # Substituir input interativo por função que simula entrada de dados
    def obter_entrada(prompt):
        print(prompt)
        return input()

    while True:
        print("=== Sistema de Cadastro de Clientes ===")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Sair")
        try:
            opcao = obter_entrada("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_cliente(clientes)
                salvar_dados(arquivo, clientes)
            elif opcao == "2":
                listar_clientes(clientes)
            elif opcao == "3":
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.\n")
        except OSError as e:
            print(f"Erro de entrada/saída: {e}")
            break

if __name__ == "__main__":
    main()
