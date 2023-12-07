#colecao de itens que possuem chave e valor
#possuem chave(keys) e valor(values)
#parametro: dic = {} ou dic = dict()
#não pode fatiar 
#não é ordenado

#ele n se importa com o valor, apenas a chave
pessoa = {'nome' : 'Lara', 
          'sobrenome' : 'Gabi',
          'sobrenome' : 'Gabi2',
          'Lara' : 'gabi',
          'Gabi' : 'sobrenome'
          } 

print(len(pessoa))
print(pessoa.keys()) #chave
print(pessoa.values()) #valor

chave = pessoa.keys() #entrega todas as chaves
valor = pessoa.values() #entrega todos valores

for cha in pessoa.keys(): #entrega todas as chaves
    print(cha)

print('=' * 20)

for v in pessoa.values(): #entrega todos valores
    print(v)

print('=' * 20)

for v, cha in pessoa.items(): #entra todas as chaves e valores
    print(v, chave)

print('=' * 20)

i = pessoa.items() 
print(i)

print('=' * 20)

print(pessoa['sobrenome'])

print('=' * 20)

d1 = {'valor1':100,
      'valor2': 200,}

print(d1)

d2 = d1.copy() #copia o dic com novo endereco de memoria

d2['valor2'] = 3000
print(f'{d1}{d2}')

print(d2.get('valor2'))  #get entrega um valor referenciado pela chave

d3 = d1.pop('valor2') #usa a mesma funcao do del
print(d3)

#adicionando #att dicionario com dicionario
outro_nome = {'valor5' : 5}
d1.update(outro_nome)
print(d1)

d4 = d1.has_key(100)
print(d4)

#del - exclui a chave - del.dic[]
#sorted - otdena um dicionario pelas duas chaves