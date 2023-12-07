marca = input('informe o marca do seu carro: ')
modelo = input('informe o modelo do seu carro: ')

lista_carros = []
lista_carros.append(marca)
lista_carros.append(modelo)
print(lista_carros)

dic_carros = {}
dic_carros.update([lista_carros])
dic_carros['Fiat'] = 'Uno'
print(dic_carros)