
agenda = {
    'dia nao existente':['000'],
    'Segunda-feira': ['09:00', '10:00', '14:00', '15:00'],
    'Terça-feira': ['10:00', '11:00', '14:00', '15:00'],
    'Quarta-feira': ['09:00', '10:00', '14:00', '15:00'],
    'Quinta-feira': ['10:00', '11:00', '14:00', '15:00'],
    'Sexta-feira': ['09:00', '10:00', '14:00', '15:00'],
}

def marcar_horario(dia, horarios):
    if dia in agenda and horarios in agenda[dia]:
        agenda[dia].remove(horarios)
        print(f"Horário {horarios} no(a) {dia} marcado com sucesso.")
    else:
        print("Horário indisponível.")






def marc():
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

    if dia_escolhido and horario_escolhido:
        marcar_horario(dia_escolhido, horario_escolhido)
    else:
        print("Escolha inválida.")
while True:
    marc()
    escolha  =int(input('Deseja continuar [1 - Sim / 2 - Não]? '))
    if escolha == 2:
        break
 
