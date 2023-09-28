from operacoes import autenticar, calcular, numero, num

def calculadora():
    print('''
    1. Soma 
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Potenciação''')
    escolha = int(input('Escolha qual opção você quer: '))
    numero1 = float(input('Digite um numero: '))
    numero2 = float(input('Digite um numero: '))
    print(f'O resultado foi de: {calcular(numero1, numero2, escolha)}')

def positivoNegativo():
    numero1 = int(input('Digite um numero: '))
    numero(numero1)

def tamanhoNumero():
    numero = int(input('Insira um numero: '))
    quantidadeDeDigitos = len(str(numero))
    num(quantidadeDeDigitos)

def cadastro():
    login = input('Insira seu nome de usuario: ')
    senha = input('Insira sua senha: ')
    autenticar(login, senha)

while True:
    opcao = int(input('''
    Digite sua opção desejada: 
    1 - Saber se o numero é positivo ou negativo: 
    2 - Quantidade de digitos:
    3 - Calculadora:
    4 - Cadastro:
    
    '''))
    if opcao == 1:
        positivoNegativo()
    elif opcao == 2:
        tamanhoNumero()
    elif opcao == 3:
        calculadora()
    elif opcao == 4:
        cadastro()
    else: 
        pass
    escolha = input('Voce deseja continuar [S/N]? ')
    if escolha.lower() == 'n':
        print('FIM')
        break
    




