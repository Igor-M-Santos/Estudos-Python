pedido = []

while True:
    try:
        nome_prato = input('Qual é o nome do prato? ')
        if nome_prato == 'sair' or nome_prato == '':
            break
        valor = float(input('Qual o valor deste item? '))
        dados_item = {'nome': nome_prato, 'preço': valor}
        
    except:
        print('Erro: Entrada inválida! Por favor, digite apenas números.')
        continue
    if valor == 0:
        break
    if valor < 0:
        print('Valor incorreto!')
        continue

    pedido.append(dados_item)

total_bruto = 0

print('--- RESUMO DO PEDIDO ---')
for item in pedido:
    print(f'- {item['nome']}: R$ {item['preço']:.2f}')
    total_bruto += item['preço']
print('-' * 28)

if total_bruto >= 150:
    desconto = total_bruto - 15
    print('Desconto de R$15 aplicado!')
else:
    desconto = total_bruto

print(f'O valor total do seu pedido: {desconto:.2f}')
print(f'Você comprou {len(pedido)} itens hoje')
