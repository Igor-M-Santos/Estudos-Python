nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
altura = float(input('Qual é a sua altura? '))
habilitacao = input('Você tem habilitação? ').lower() == 'sim'

print(f'Nome: {type(nome)}')
print(f'Idade: {type(idade)}')
print(f'Altura: {type(altura)}')
print(f'Habilitação: {type(habilitacao)}')