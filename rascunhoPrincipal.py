import sys


barbeiro1 = [{'Nome': 'Joao Alberto'}]
barbeiro2 = [{'Nome': 'Guilherme Alencar'}]
agenda = {
    'dia nao existente':['000'],
    'Segunda-feira': ['09:00', '10:00', '14:00', '15:00'],
    'Terça-feira': ['10:00', '11:00', '14:00', '15:00'],
    'Quarta-feira': ['09:00', '10:00', '14:00', '15:00'],
    'Quinta-feira': ['10:00', '11:00', '14:00', '15:00'],
    'Sexta-feira': ['09:00', '10:00', '14:00', '15:00'],
}

cabelo = {'Cabelo': 15}
cabeloSobrancelha = [{'Cabelo e sobrancelha': 20}]
cabeloSobrancelhaBarba = [{'Cabelo, sobrancelhae e barba': 35}]
sobrancelha = [{'Sobrancelha': 7}]
barba = [{'Barba': 15}]
cabeloBarba = [{'Cabelo e barba': 30}]
barbaterapia = [{'Barbaterapia e corte': 50}]
platinar = [{'Platinar e corte': 100}]
#função para retornar os cortes e os valores que foram inseridos nela
def corte(cabelo, cabeloSobrancelha, cabeloSobrancelhaBarba, barbaterapia, sobrancelha, barba, cabeloBarba, platinar):
    escolha = int(input('''\nEsolha um dos serviços abaixo: 
            1. Cabelo: R$15
            2. Cabelo + sobrancelha: R$20
            3. Cabelo + Barba: R$30
            4. Cabelo + Sobrancelha + Barba: R$35
            5. Sobrancelha: R$7 
            6. Barba: R$15
            7. Barbaterapia + Corte: R$50
            8. Platinar + Corte: R$100
            : ''')) 
    if escolha == 1:
        return cabelo
    elif escolha == 2:
        return cabeloSobrancelha
    elif escolha == 3:
        return cabeloBarba
    elif escolha == 4:
        return cabeloSobrancelhaBarba
    elif escolha == 5:
        return sobrancelha
    elif escolha == 6:
        return barba
    elif escolha == 7:
        return barbaterapia
    elif escolha == 8:
        return platinar
def marcarCorte():
    global dia_escolhido
    global horario_escolhido
    dia = input('''Escolha o dia: 
                    1 - Segunda
                    2 - Terça
                    3 - Quarta
                    4 - Quinta
                    5 - Sexta
                    : ''')
    horarios = input('''Escolha agora o horário: 
                    1 - 09:00
                    2 - 10:00
                    3 - 11:00
                    4 - 12:00
                    : ''')
    dias_semana = {
        '1': 'Segunda-feira',
        '2': 'Terça-feira',
        '3': 'Quarta-feira',
        '4': 'Quinta-feira',
        '5': 'Sexta-feira',
    }
    horarios_disponiveis = {
        '1': '09:00',
        '2': '10:00',
        '3': '11:00',
        '4': '12:00',
    }
    dia_escolhido = dias_semana.get(dia)
    horario_escolhido = horarios_disponiveis.get(horarios)

    if dia_escolhido in agenda and horario_escolhido in agenda[dia_escolhido]:
        agenda[dia_escolhido].remove(horario_escolhido)
        print(f"Horário {horario_escolhido} no(a) {dia_escolhido} marcado com sucesso.")
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f'/{dia_escolhido}/{horario_escolhido}\n')
    else:
        print('Marque novamente.')
        print("Horário indisponível.")
        print()
        marcarCorte()
#função para realizar um cadastro
def register():
    global dia_escolhido
    global horario_escolhido
    usuario = input('Digite um e-mail ou nome de usuario para salvar seus cortes: ')
    senha = input('Crie sua senha: ')
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f'\n{usuario}:{senha}')

    print("Usuário cadastrado com sucesso!")
#função do login para ter acesso à função barbeiro
def login():
    usuario = input('Digite seu e-mail ou nome de usuário para acessar a página: ')
    senha = input('Insira sua senha: ')

    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    # Verifica se as credenciais correspondem a algum usuário
    for linha in linhas:
        partes = linha.strip().split(":")
        if len(partes) == 2:
            nome, senha_salva = partes
            if nome == usuario and senha_salva == senha:
                print('Acesso permitido.')
                print()
                barbeiro(barbeiro1, barbeiro2)
                return

    print("Acesso negado.")

def visualizarCliente():
    with open('usuarios.txt' , 'r') as arquivo:
        visualizar = arquivo.readlines()
        print(visualizar)
#função principal onde agenda o corte
def barbeiro(barbeiro1, barbeiro2):
    barber1 = 'João Alberto'
    barber2 = 'Guilerme Alencar'
    global loginn 
    global princ
    princ = []
    #dicionaro que serviu para guardar o serviço escolhido pelo cliente e conseguir aparecer na mensagem final
    descricao_servicos = {
    1: 'Cabelo',
    2: 'Cabelo + sobrancelha',
    3: 'Cabelo + Barba',
    4: 'Cabelo + Sobrancelha + Barba',
    5: 'Sobrancelha',
    6: 'Barba',
    7: 'Barbaterapia + Corte',
    8: 'Platinar + Corte'
}
    nome = input('\nInsira seu nome: ')
    selecionar = int(input(f'\nQual dos barbeiros fará o serviço [1 - {barber1} / 2 - {barber2}]? '))
    if selecionar == 1:
        print(f'\nMuito bem {nome} escolha um serviço por favor:')
        barbeiro1 = [{'Nome': 'Joao'} , {'Cliente': nome}, {'Serviço': corte(cabelo, cabeloSobrancelha, cabeloSobrancelhaBarba, barbaterapia, sobrancelha, barba, cabeloBarba, platinar)}]
        servicoSelecionado = {'Servico': selecionar}
        descricao_servicos = descricao_servicos.get(selecionar, 'Serviço não encontrado')
        marcarCorte()
    
        for barbeiro, servico in servicoSelecionado.items():
            print(f'O cliente {nome} selecionou o serviço de {descricao_servicos} com o barbeiro {barber1}')
            print()
        princ.append(barbeiro1.copy())
        barbeiro1.clear()
    elif selecionar == 2:
        print(f'\nMuito bem {nome} escolha um serviço por favor:')
        barbeiro2 = [{'Nome': 'Guilherme'}, {'Cliente': nome}, {'Serviço': corte(cabelo, cabeloSobrancelha, cabeloSobrancelhaBarba, barbaterapia, sobrancelha, barba, cabeloBarba, platinar)}]
        servicoSelecionado = {'Servico': selecionar}
        descricao_servicos = descricao_servicos.get(selecionar, 'Serviço não encontrado')

        for barbeiro, servico in servicoSelecionado.items():
            print(f'O cliente {nome} selecionou o serviço de {descricao_servicos} com o barbeiro {barber2}')
        print()
        princ.append(loginn.copy())
        princ.append(barbeiro2.copy())
        barbeiro1.clear()
        print(princ)
    else: 
        pass
    print('Obrigado pela preferencia, aguardamos você.')
    print()
    
        
#função que deixei de usar mas não vou excluir para também usar como base as excessões
def cadastro():
    try:
        escolha = int(input('Ola, você gostaria de marcar um horário [1 - Sim / 2 - Não]? '))
        print()
        if escolha == 1:
            barbeiro(barbeiro1, barbeiro2)
        elif escolha == 2:
            sys.exit()
    except ValueError:
        print('Por favor nos informe um numero [1 ou 2], e não uma letra ou palavra :).')
        print()
        escolha = int(input('Voce deseja tentar novamente [1 - Sim / 2 - Não]? '))
        if escolha == 2:
            print('Obrigado')
            sys.exit()

#Função menu principal

def menu():
    while True:
        opcao = int(input('''Qual opção voce deseja?

        1. Cadastro
        2. Login
        3. Ver clientes
        4. Sair
        : '''))   
        match opcao:
            case 1:
                register()
            case 2:
                login()
            case 3:
                visualizarCliente()
            case 4:
                print('Voce saiu do programa.')
                sys.exit()
            case _:
                print('Opção invalida')


menu()

        
    

