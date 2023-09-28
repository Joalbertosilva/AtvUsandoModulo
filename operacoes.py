def autenticar(login, senha):
    usuarios = [
      {
         'Username': 'teste',
         'Senha': 'admin'
      },
      {
         'Username': 'teste2',
         'Senha': 'admin2'
      },
       {
         'Username': 'teste3',
         'Senha': 'admin3'
      },
      {
         'Username': 'teste4',
         'Senha': 'admin4'
      }
   ]
    for usuario in usuarios:
        if login == usuario['Username'] and senha == usuario['Senha']:
            print('Voce acessou!')
            return
    print('Dados incorretos!')

def soma(numero1, numero2):
    return numero1 + numero2

def sub(numero1, numero2):
    return numero1 - numero2

def multi(numero1, numero2):
    return numero1 * numero2

def divi(numero1, numero2):
    return numero1 / numero2

def potencia(numero1, numero2):
    return numero1 ** numero2

def calcular(numero1, numero2, escolha):
    if escolha == 1:
        return soma(numero1, numero2)
    elif escolha == 2:
        return sub(numero1, numero2)
    elif escolha == 3:
        return multi(numero1, numero2)
    elif escolha == 4:
        return divi(numero1, numero2)
    elif escolha == 5:
        return potencia(numero1, numero2)
    else:
        pass

def numero(numero1):
    if numero1 >= 0:
        print('P')
    else:
        print('N')

def num(quantidadeDeDigitos):
   print(quantidadeDeDigitos)
   



