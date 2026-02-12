produtos_da_loja = ("Notebook", "Mouse", "Teclado", "Monitor", "Headset")
vendas_do_dia = ["Mouse", "Monitor"]

precisa_repor = [produto for produto in produtos_da_loja if produto in vendas_do_dia]

print(precisa_repor)