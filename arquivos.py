#nome = input('Insira seu nome: ')
nome = input('Insira seu nome: ')
name = nome
idad = input('Insira sua idade: ')
idade = idad
with open('test.txt', 'a', encoding="utf-8") as arquivo:
    arquivo.write(f'\n Nome: {name}, Idade: {idade}')
with open('test.txt', 'r', encoding="utf-8", errors="ignore") as ler:
    linhas = ler.readlines() 
    print(linhas)


