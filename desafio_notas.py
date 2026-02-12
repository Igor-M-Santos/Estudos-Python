notas = [7.5, 8.0, 6.5, 9.0]
notas.append(10.0)
nota_com_bonus = []

media = sum(notas) / len(notas)

print(f'A maior nota foi: {max(notas)}')
print(f'A menor nota foi: {min(notas)}')
print(f'Média: {media:.1f}')

aprovados = 0

for n in notas:
    nova_nota = n + 0.5
    if nova_nota > 10:
        nova_nota = 10 
    
    nota_com_bonus.append(nova_nota)

    if n >= 7:
        aprovados += 1 

    if n >= 9.0:
        print(f'Nota: {n} Aluno destaque')
    elif n >= 7:
        print(f'Nota: {n} Aluno aprovado')
    else:
        print(f'Nota: {n} Aluno reprovado')

porcentagem = (aprovados / len(notas)) * 100

print(f'notas com bonus: {nota_com_bonus}')
print(f'Total de aprovados: {aprovados}')
print(f'Taxa de aprovação: {porcentagem}%')





























    

