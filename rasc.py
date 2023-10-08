import sys

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Abre o arquivo em modo de escrita (append) para adicionar o novo usuário
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario}:{senha}\n")

    print("Usuário cadastrado com sucesso!")

# Função para fazer login
def fazer_login():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Abre o arquivo em modo de leitura para verificar os usuários cadastrados
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    # Verifica se as credenciais correspondem a algum usuário
    for linha in linhas:
        partes = linha.strip().split(":")
        if len(partes) == 2:
            nome, senha_salva = partes
            if nome == usuario and senha_salva == senha:
                print("Acesso permitido!")
                return

    print("Acesso negado.")

# Menu principal
while True:
    print("\nOpções:")
    print("1. Cadastrar novo usuário")
    print("2. Fazer login")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        fazer_login()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")