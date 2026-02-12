# rendimento_mensal = float(input('Qual é o seu rendimento mensal? '))
# parcela = int(input('Parcela desejada: '))
# tempo_de_servico = int(input('Tempo de serviço(em meses): '))

# if parcela <= (rendimento_mensal * 0.30) and tempo_de_servico >= 12:
#     print('Empréstimo aprovado!')
# elif parcela <= (rendimento_mensal * 0.30) and tempo_de_servico < 12:
#     print('Negado: Seu tempo de serviço precisa ser de 12 meses para que o empréstimo seja aprovado')
# elif parcela > (rendimento_mensal * 0.30) and tempo_de_servico >= 12:
#     print('Negado: a parcela é maior do que trinta porcento do seu rendimento mensal')
# else: 
#     print('Negado: seu tempo de serviço é menor que 12 messes e sua parcela é maior que o seu rendimento mensal')

# lado1 = float(input('Digite um número: '))
# lado2 = float(input('Digite um número: '))
# lado3 = float(input('Digite um número: '))

# if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
#         print('Valor inválido')
# else:
     
#     if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1): 
#         if lado1 == lado2 == lado3:
#          print('tipo: equilátero')
#         elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
#             print('tipo: escaleno')
#         else:
#             print('tipo: isósceles') 

#     else:
#      print('os valores informados não podem formar um triângulo')




lado1 = float(input('lado1: '))
lado2 = float(input('lado2: '))
lado3 = float(input('lado3: '))

if lado1 <= 0 or lado2 <=0 or lado3 <=0:
    print('Valor inválido, tente novamente')
else:
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            print('Equilátero')
        elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
            print('Escaleno')
        else:
            print('Isósceles')
    else:
        print('Os valores inseridos não podem formar um triângulo')



























 


