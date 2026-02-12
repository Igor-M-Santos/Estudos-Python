precos = [150.0, 90.0, 300.0, 50.0, 450.0]
precos_com_desconto = []
total_desconto  = 0
economia_total = 0

for preco in precos:
    if preco > 200:
        novo_preco = preco * 0.85
        total_desconto += 1
        economia = preco - novo_preco
        economia_total += economia
        print(f'O prduto de R$ {preco} ganhou desconto e caiu para R$ {novo_preco:.2f}')   
    else:
        novo_preco = preco

    precos_com_desconto.append(novo_preco)

print(f'--- Relatório de Vendas ---')
print(f'Preços finais: {precos_com_desconto}')
print(f'Total de produtos com desconto: {total_desconto}')
print(f'Valor total economizado: R$ {economia_total:.2f}')
print(f'Valor total da folha: R$ {sum(precos_com_desconto):.2f}')


